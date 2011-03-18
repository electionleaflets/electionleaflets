from django.db import models
from parties.models import Party
from constituencies.models import Constituency
from categories.models import Category
from tags.models import Tag   


class UploadSession(models.Model):
    key = models.CharField( max_length=64, null=True, blank=True )
    image1 = models.ImageField( upload_to='uploads/', null=True, blank=True )
    image2 = models.ImageField( upload_to='uploads/',null=True, blank=True )
    image3 = models.ImageField( upload_to='uploads/',null=True, blank=True )
    image4 = models.ImageField( upload_to='uploads/',null=True, blank=True )
    image5 = models.ImageField( upload_to='uploads/',null=True, blank=True )
    image6 = models.ImageField( upload_to='uploads/',null=True, blank=True )
    image7 = models.ImageField( upload_to='uploads/',null=True, blank=True )
    image8 = models.ImageField( upload_to='uploads/',null=True, blank=True )
    s3keys = models.TextField(null=True, blank=True)
    
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
    leaflet = models.ForeignKey(Leaflet, related_name='images')
    image_key = models.CharField(max_length=765)
    sequence = models.IntegerField()
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

