from django.db import models
from parties.models import Party
from constituencies.models import Constituency
from categories.models import Category
from tags.models import Tag   

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
    
    def get_first_image(self):
        return self.images.all()[0]

    def get_first_constituency(self):
        return self.constituencies.all()[0]
    
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



class LeafletElectionSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'leaflet_election__seq'


class LeafletImageSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'leaflet_image_seq'

class LeafletPartyAttack(models.Model):
    leaflet_party_attack_id = models.IntegerField(primary_key=True)
    leaflet_id = models.IntegerField()
    party_id = models.IntegerField()
    class Meta:
        db_table = u'leaflet_party_attack'

class LeafletPartyAttackSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'leaflet_party_attack_seq'

class LeafletSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'leaflet_seq'



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

