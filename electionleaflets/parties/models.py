from django.db import models
from core.models import Country

#TODO: Add auto-slug

class Party(models.Model):
    name = models.CharField(max_length=128)
    country = models.ForeignKey( Country )
    logo_file = models.CharField(max_length=300, blank=True)
    url = models.URLField(blank=True)
    colour = models.CharField(max_length=18, blank=True)
    twitter_account = models.CharField(max_length=150, blank=True)
