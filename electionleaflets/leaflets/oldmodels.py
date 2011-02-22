# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class OldBoundariesBoundary(models.Model):
    id = models.IntegerField(primary_key=True)
    constituency_id = models.IntegerField()
    boundary = models.TextField()
    zoom = models.IntegerField()
    north = models.FloatField()
    south = models.FloatField()
    east = models.FloatField()
    west = models.FloatField()
    class Meta:
        db_table = u'boundaries_boundary'

class OldCategory(models.Model):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.TextField(blank=True)
    default_value = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'category'

class OldConstituency(models.Model):
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

class OldConstituencySeq(models.Model):
    sequence = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'constituency_seq'

class OldConstituencyType(models.Model):
    constituency_type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    country_id = models.IntegerField()
    url_id = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'constituency_type'

class OldCountry(models.Model):
    country_id = models.IntegerField(primary_key=True)
    iso = models.CharField(max_length=6)
    name = models.CharField(max_length=240)
    iso3 = models.CharField(max_length=9, blank=True)
    class Meta:
        db_table = u'country'

class OldEmailAlert(models.Model):
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

class OldEmailAlertSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'email_alert_seq'

class OldEmailQue(models.Model):
    email_que_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765, blank=True)
    email = models.CharField(max_length=765)
    postcode = models.CharField(max_length=60)
    delivery_date = models.DateTimeField()
    class Meta:
        db_table = u'email_que'

class OldImageQue(models.Model):
    image_que_id = models.IntegerField(primary_key=True)
    upload_key = models.CharField(max_length=765)
    name = models.CharField(max_length=300, blank=True)
    email = models.CharField(max_length=300, blank=True)
    image_key = models.CharField(max_length=765, blank=True)
    uploaded_date = models.DateTimeField()
    class Meta:
        db_table = u'image_que'

class OldImageQueSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'image_que_seq'

class OldLeaflet(models.Model):
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
        
class OldLeafletCategory(models.Model):
    leaflet_category_id = models.IntegerField(primary_key=True)
    leaflet_id = models.IntegerField()
    category_id = models.IntegerField()
    class Meta:
        db_table = u'leaflet_category'


class OldLeafletCategorySeq(models.Model):
    sequence = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'leaflet_category_seq'

class OldLeafletConstituency(models.Model):
    leaflet_constituency_id = models.IntegerField(primary_key=True)
    leaflet_id = models.IntegerField()
    constituency_id = models.IntegerField()
    class Meta:
        db_table = u'leaflet_constituency'

class OldLeafletConstituencySeq(models.Model):
    sequence = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'leaflet_constituency_seq'

class OldLeafletElectionSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'leaflet_election__seq'

class OldLeafletImage(models.Model):
    leaflet_image_id = models.IntegerField(primary_key=True)
    leaflet_id = models.IntegerField()
    image_key = models.CharField(max_length=765)
    sequence = models.IntegerField()
    class Meta:
        db_table = u'leaflet_image'

class OldLeafletImageSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'leaflet_image_seq'

class OldLeafletPartyAttack(models.Model):
    leaflet_party_attack_id = models.IntegerField(primary_key=True)
    leaflet_id = models.IntegerField()
    party_id = models.IntegerField()
    class Meta:
        db_table = u'leaflet_party_attack'

class OldLeafletPartyAttackSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'leaflet_party_attack_seq'

class OldLeafletSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'leaflet_seq'

class OldLeafletTag(models.Model):
    leaflet_tag_id = models.IntegerField(primary_key=True)
    leaflet_id = models.IntegerField()
    tag_id = models.IntegerField()
    class Meta:
        db_table = u'leaflet_tag'

class OldLeafletTagSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'leaflet_tag_seq'

class OldParty(models.Model):
    party_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    country_id = models.IntegerField()
    major = models.IntegerField(null=True, blank=True)
    logo_file = models.CharField(max_length=300, blank=True)
    url_id = models.CharField(max_length=765, blank=True)
    colour = models.CharField(max_length=18, blank=True)
    twitter_account = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = u'party'

class OldPromise(models.Model):
    promise_id = models.IntegerField(primary_key=True)
    leaflet_id = models.IntegerField()
    detail = models.TextField()
    class Meta:
        db_table = u'promise'

class OldRateInteresting(models.Model):
    rate_interesting_id = models.IntegerField(primary_key=True)
    leaflet_id = models.IntegerField()
    description = models.TextField()
    user_name = models.CharField(max_length=765)
    user_email = models.CharField(max_length=765)
    class Meta:
        db_table = u'rate_interesting'

class OldRateInterestingSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'rate_interesting_seq'

class OldRateType(models.Model):
    rate_type_id = models.IntegerField(primary_key=True)
    left_label = models.CharField(max_length=150)
    right_label = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = u'rate_type'

class OldRateValue(models.Model):
    rate_value_id = models.IntegerField(primary_key=True)
    leaflet_id = models.IntegerField()
    user_name = models.CharField(max_length=300)
    user_email = models.CharField(max_length=300)
    rate_type_id = models.IntegerField()
    value = models.IntegerField()
    class Meta:
        db_table = u'rate_value'

class OldRateValueSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'rate_value_seq'

class OldTag(models.Model):
    tag_id = models.IntegerField(primary_key=True)
    tag = models.CharField(max_length=765)
    tag_clean = models.CharField(max_length=765, blank=True)
    dead = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'tag'

class OldTagSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'tag_seq'

