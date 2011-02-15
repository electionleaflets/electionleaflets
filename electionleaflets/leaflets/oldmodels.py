# This file exists solely to map to the existing UK electionleaflets database
# to enable us to more easily port the data from the existing database 
# structure to the more django-ified structure.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.TextField(blank=True)
    default_value = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'category'

class Constituency(models.Model):
    constituency_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    alternative_name = models.CharField(max_length=765, blank=True)
    constituency_type_id = models.IntegerField()
    retired = models.IntegerField(null=True, blank=True)
    area_code = models.CharField(max_length=60, blank=True)
    area_uri = models.CharField(max_length=765, blank=True)
    wikipedia_url = models.CharField(max_length=765, blank=True)
    url_id = models.CharField(max_length=300, blank=True)
    guardian_aristotle_id = models.IntegerField(null=True, blank=True)
    guardian_pa_code = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'constituency'

class ConstituencyType(models.Model):
    constituency_type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    country_id = models.IntegerField()
    url_id = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'constituency_type'

class Country(models.Model):
    country_id = models.IntegerField(primary_key=True)
    iso = models.CharField(max_length=6)
    name = models.CharField(max_length=240)
    iso3 = models.CharField(max_length=9, blank=True)
    class Meta:
        db_table = u'country'

class EmailAlert(models.Model):
    email_alert_id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=150)
    frequency_hours = models.IntegerField()
    last_sent = models.DateTimeField(null=True, blank=True)
    type = models.CharField(max_length=150)
    parent_id = models.IntegerField()
    activated = models.IntegerField(null=True, blank=True)
    confirm_id = models.CharField(max_length=300)
    title = models.CharField(max_length=765)
    class Meta:
        db_table = u'email_alert'

class EmailQue(models.Model):
    email_que_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765, blank=True)
    email = models.CharField(max_length=765)
    postcode = models.CharField(max_length=60)
    delivery_date = models.DateTimeField()
    class Meta:
        db_table = u'email_que'

class ImageQue(models.Model):
    image_que_id = models.IntegerField(primary_key=True)
    upload_key = models.CharField(max_length=765)
    name = models.CharField(max_length=300, blank=True)
    email = models.CharField(max_length=300, blank=True)
    image_key = models.CharField(max_length=765, blank=True)
    uploaded_date = models.DateTimeField()
    class Meta:
        db_table = u'image_que'

class Leaflet(models.Model):
    leaflet_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=765)
    description = models.TextField(blank=True)
    publisher_party_id = models.IntegerField()
    postcode = models.CharField(max_length=150, blank=True)
    lng = models.FloatField()
    lat = models.FloatField()
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    date_uploaded = models.DateTimeField()
    date_delivered = models.DateTimeField()
    live = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'leaflet'

class LeafletCategory(models.Model):
    leaflet_category_id = models.IntegerField(primary_key=True)
    leaflet_id = models.IntegerField()
    category_id = models.IntegerField()
    class Meta:
        db_table = u'leaflet_category'

class LeafletCategorySeq(models.Model):
    sequence = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'leaflet_category_seq'

class LeafletConstituency(models.Model):
    leaflet_constituency_id = models.IntegerField(primary_key=True)
    leaflet_id = models.IntegerField()
    constituency_id = models.IntegerField()
    class Meta:
        db_table = u'leaflet_constituency'

class LeafletElectionSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'leaflet_election__seq'

class LeafletImage(models.Model):
    leaflet_image_id = models.IntegerField(primary_key=True)
    leaflet_id = models.IntegerField()
    image_key = models.CharField(max_length=765)
    sequence = models.IntegerField()
    class Meta:
        db_table = u'leaflet_image'

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
    leaflet_tag_id = models.IntegerField(primary_key=True)
    leaflet_id = models.IntegerField()
    tag_id = models.IntegerField()
    class Meta:
        db_table = u'leaflet_tag'

class LeafletTagSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'leaflet_tag_seq'

class Party(models.Model):
    party_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    country_id = models.IntegerField()
    logo_file = models.CharField(max_length=300, blank=True)
    url_id = models.CharField(max_length=765, blank=True)
    colour = models.CharField(max_length=18, blank=True)
    twitter_account = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = u'party'

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

class Tag(models.Model):
    tag_id = models.IntegerField(primary_key=True)
    tag = models.CharField(unique=True, max_length=765)
    class Meta:
        db_table = u'tag'

class TagSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'tag_seq'

