from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=240)
    iso = models.CharField(max_length=6)
    iso3 = models.CharField(max_length=9, blank=True)
