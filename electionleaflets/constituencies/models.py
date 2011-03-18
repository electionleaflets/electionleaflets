from django.db import models
from core.util import AutoSlugField
from core.models import Country

class ConstituencyType(models.Model):
    name = models.CharField(max_length=150)
    country = models.ForeignKey(Country)
    url_id = models.CharField(max_length=300, blank=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = u'constituency_type'


class Constituency(models.Model):
    name = models.CharField(max_length=765)
    alternative_name = models.CharField(max_length=765, blank=True)
    constituency_type = models.ForeignKey(ConstituencyType)
    retired = models.IntegerField(null=True, blank=True)
    area_code = models.CharField(max_length=60, blank=True)
    area_uri = models.CharField(max_length=765, blank=True)
    wikipedia_url = models.CharField(max_length=765, blank=True)
    url_id = models.CharField(max_length=300, blank=True)
    guardian_aristotle_id = models.IntegerField(null=True, blank=True)
    guardian_pa_code = models.IntegerField(null=True, blank=True)
    slug = AutoSlugField( populate_from='name', max_length=255)
    class Meta:
        db_table = u'constituency'
        verbose_name_plural = 'Constituencies'
        
    def __unicode__(self):
        return self.name

