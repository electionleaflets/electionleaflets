from django.db import models
from core.models import Country


class Party(models.Model):
    name = models.CharField(max_length=765)
    country = models.ForeignKey(Country)
    major = models.IntegerField(null=True, blank=True)
    logo_file = models.CharField(max_length=300, blank=True)
    url_id = models.CharField(max_length=765, blank=True)
    colour = models.CharField(max_length=18, blank=True)
    twitter_account = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = u'party'
