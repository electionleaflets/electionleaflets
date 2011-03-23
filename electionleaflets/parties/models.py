from django.db import models
from core.models import Country
from core.util import AutoSlugField

class Party(models.Model):
    name = models.CharField(max_length=765)
    country = models.ForeignKey(Country)
    major = models.IntegerField(null=True, blank=True)
    logo_file = models.CharField(max_length=300, blank=True)
    url_id = models.CharField(max_length=765, blank=True)
    colour = models.CharField(max_length=18, blank=True)
    twitter_account = models.CharField(max_length=150, blank=True)
    slug = AutoSlugField( populate_from='name', max_length=255,field_separator='_')
    count = models.IntegerField()
    popular = models.IntegerField()
    
    class Meta:
        db_table = u'party'
        verbose_name_plural = 'Parties'

    def __unicode__(self):
        return self.name