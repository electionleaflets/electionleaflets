from django.db import models
from parties.models import Party
from constituencies.models import Constituency
from categories.models import Category
from tags.models import Tag   
import logging

def update_filename(instance, filename):
    import uuid, os
    
    path = "uploads/"
    _,ext = os.path.splitext( filename )
    
    return os.path.join(path, str(uuid.uuid4()) + ext )    


class UploadSession(models.Model):
    key = models.CharField( max_length=64, null=True, blank=True )
    image1 = models.ImageField( upload_to=update_filename, max_length=255,null=True, blank=True )
    image2 = models.ImageField( upload_to=update_filename, max_length=255,null=True, blank=True )
    image3 = models.ImageField( upload_to=update_filename, max_length=255,null=True, blank=True )
    image4 = models.ImageField( upload_to=update_filename, max_length=255,null=True, blank=True )
    image5 = models.ImageField( upload_to=update_filename, max_length=255,null=True, blank=True )
    image6 = models.ImageField( upload_to=update_filename, max_length=255,null=True, blank=True )
    image7 = models.ImageField( upload_to=update_filename, max_length=255,null=True, blank=True )
    image8 = models.ImageField( upload_to=update_filename, max_length=255,null=True, blank=True )
    s3keys = models.TextField(null=True, blank=True)
    
    def names(self):
        vals = []
        for x in range(1,9):
            img = getattr(self, 'image%s' % x)
            if img:
                name = str(img).split('/')[-1]
                vals.append( name.split('.')[0] )
        return vals
    
    def resize_file( self, fl, name, w, h):
        from PIL import Image        
        from django.conf import settings
        import os

        x = w
        y = h
        
        srcpath = os.path.join( settings.MEDIA_ROOT, str(fl))
        path,ext = os.path.splitext( srcpath )
        parts = path.split('/')
        outpath = '/'.join(parts[:-1])
        outpath = os.path.join(outpath, name)
        outpath = os.path.join(outpath, parts[-1])        
        outpath = outpath + ext
        
        try:
            f = open( srcpath, 'rb' )
            image = Image.open( f )
            if image.mode not in ("L", "RGB"):
                image = image.convert("RGB")                    
            
            img_ratio = float(image.size[0]) / image.size[1]
            if x==0.0:
                x = y * img_ratio
            elif y==0.0:
                y = x / img_ratio            
            resize_ratio = float(x) / y
            x = int(x)
            y = int(y)
        
            img = image.resize( (x,y,) )
            img.save(outpath, "JPEG")

        except:
            return None
        
        return outpath
    
    def handle_file_uploads( self ):
        for x in range(1,9):
            img = getattr(self, 'image%s' % x)
            if img:
                f = self.resize_file( img, 'thumbnail', 140, 0 )                
                self.send_to_s3( f, "thumbnail")
                
                f = self.resize_file( img, 'small', 120, 0 )
                self.send_to_s3( f, "small")
                
                f = self.resize_file( img, 'medium', 300, 0 )
                self.send_to_s3( f, "medium")
                
                f = self.resize_file( img, 'large', 1024, 0 )                                
                self.send_to_s3( f, "large")                
    
    def send_to_s3(self,filename, folder):
        """
        Send the source file, filename, to S3 (if enabled) and store it in 
        the named folder.
        """
        from django.conf import settings
        from third_party import S3
                
        import mimetypes
        import os.path
        import sys
        
        if not settings.S3_ENABLED:
            return
        
        if filename is None:
            # TODO: We need to log the error (and alert an admin)
            return
        
        try:
            conn = S3.AWSAuthConnection(settings.AWS_KEY, settings.AWS_SECRET)
            filedata = open(filename, 'rb').read()
            content_type = 'image/jpeg'
        
            newname = '%s/%s' % (folder,os.path.basename(filename),)
            #logging( "Uploading %s as %s" % (filename,newname,)
        
            conn.put(settings.S3_BUCKET, newname, S3.S3Object(filedata),
                {'x-amz-acl': 'public-read', 'Content-Type': content_type})
            del conn
        except:
            logging.error( "Unexpected error:", sys.exc_info()[0])
    
    
    
class LeafletConstituency(models.Model):
    leaflet = models.ForeignKey('Leaflet')
    constituency = models.ForeignKey(Constituency)
    
    class Meta:
        db_table='leaflet_constituency'    
   
   
class Leaflet(models.Model):
    title = models.CharField(max_length=765)
    description = models.TextField(blank=True)
    publisher_party = models.ForeignKey(Party)
    constituencies = models.ManyToManyField( Constituency, through='LeafletConstituency' )
    
    attacks = models.ManyToManyField( Party, through='LeafletPartyAttack', related_name='attacks')
    tags = models.ManyToManyField( Tag, through='LeafletTag' )
    categories = models.ManyToManyField( Category, through='LeafletCategory' )    
    
    postcode = models.CharField(max_length=150, blank=True)
    lng = models.FloatField()
    lat = models.FloatField()
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    date_uploaded = models.DateTimeField()
    date_delivered = models.DateTimeField()
    live = models.IntegerField(null=True, blank=True)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        from django.contrib.sites.models import Site
        return 'http://%s/leaflets/%s/' % (Site.objects.get_current().domain,self.id)
    
    def get_first_image(self):
        try:
            return self.images.all()[0]
        except IndexError:
            # TODO: Set image_key to value for 'empty' image
            return { 'image_key': ''}
            
    def get_first_constituency(self):
        if self.constituencies.count():
            return self.constituencies.all()[0]
        else:
            return None
    
    def get_title(self):
        return self.title if self.title and len(self.title) else ('%s leaflet' % self.party.name)
    
    class Meta:
        db_table = u'leaflet'


class LeafletImage(models.Model):
    id = models.AutoField(primary_key=True)
    leaflet = models.ForeignKey(Leaflet, related_name='images')
    image_key = models.CharField(max_length=765)
    sequence = models.PositiveIntegerField()
    
    #thestraightchoice.s3
    def get_medium(self):
        return self.get_image('medium')

    def get_large(self):
        return self.get_image('large')

    def get_small(self):
        return self.get_image('small')

    def get_thumb(self):
        return self.get_image('thumbnail')

    def get_original(self):
        return self.get_image('')
        
    def get_image(self, size):
        import os
        from django.conf import settings
        
        if settings.S3_ENABLED:
            if size:
                url = "http://%s.s3.amazonaws.com/%s/%s.jpg" % (settings.S3_BUCKET, size, self.image_key,)
            else:
                url = "http://%s.s3.amazonaws.com/%s.jpg" % (settings.S3_BUCKET, self.image_key,)
        else:
            p = os.path.join(settings.MEDIA_URL, 'uploads')
            p = os.path.join(p, size)
            url = os.path.join(p, self.image_key) + '.jpg'
        return url
            
    class Meta:
        db_table = u'leaflet_image'


        
class LeafletCategory(models.Model):
    leaflet = models.ForeignKey(Leaflet)
    category = models.ForeignKey(Category)
    class Meta:
        db_table = u'leaflet_category'


class LeafletPartyAttack(models.Model):
    leaflet = models.ForeignKey(Leaflet)
    party = models.ForeignKey(Party)
    class Meta:
        db_table = u'leaflet_party_attack'


class LeafletTag(models.Model):
    leaflet = models.ForeignKey(Leaflet)
    tag = models.ForeignKey(Tag)
    class Meta:
        db_table = u'leaflet_tag'




class Promise(models.Model):
    promise_id = models.IntegerField(primary_key=True)
    leaflet_id = models.IntegerField()
    detail = models.TextField()
    class Meta:
        db_table = u'promise'

class RateInteresting(models.Model):
    rate_interesting_id = models.IntegerField(primary_key=True)
    leaflet_id = models.IntegerField()
    description = models.TextField()
    user_name = models.CharField(max_length=765)
    user_email = models.CharField(max_length=765)
    class Meta:
        db_table = u'rate_interesting'

class RateInterestingSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'rate_interesting_seq'

class RateType(models.Model):
    rate_type_id = models.IntegerField(primary_key=True)
    left_label = models.CharField(max_length=150)
    right_label = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = u'rate_type'

class RateValue(models.Model):
    rate_value_id = models.IntegerField(primary_key=True)
    leaflet_id = models.IntegerField()
    user_name = models.CharField(max_length=300)
    user_email = models.CharField(max_length=300)
    rate_type_id = models.IntegerField()
    value = models.IntegerField()
    class Meta:
        db_table = u'rate_value'

class RateValueSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'rate_value_seq'

