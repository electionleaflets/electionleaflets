from django.db import models
from parties.models import Party
from constituencies.models import Constituency
from categories.models import Category
from tags.models import Tag   

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
            pass
        
    
    def handle_file_uploads( self ):
        for x in range(1,9):
            img = getattr(self, 'image%s' % x)
            if img:
                self.resize_file( img, 'thumbs', 140, 0 )                
                self.resize_file( img, 'small', 120, 0 )
                self.resize_file( img, 'medium', 300, 0 )
                self.resize_file( img, 'large', 1024, 0 )                                
    
    
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
    
    def get_first_image(self):
        try:
            return self.images.all()[0]
        except IndexError:
            # TODO: Set image_key to value for 'empty' image
            return { 'image_key': ''}
            
    def get_first_constituency(self):
        return self.constituencies.all()[0]
    
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
        return self.get_image('thumbs')

    def get_original(self):
        return self.get_image('')
        
    def get_image(self, size):
        import os
        from django.conf import settings
        
        p = os.path.join(settings.MEDIA_URL, 'uploads')
        p = os.path.join(p, size)
        return os.path.join(p, self.image_key) + '.jpg'

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

