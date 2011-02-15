from django.db import models
from parties.models import Party
   

class Leaflet(models.Model):
    title = models.CharField( max_length=255 )
    description = models.TextField( blank=True )
    publishing_party = models.ForeignKey( Party )
    postcode = models.CharField(max_length=12, blank=True)
    lng = models.FloatField()
    lat = models.FloatField()
    date_uploaded = models.DateTimeField()
    date_delivered = models.DateTimeField()
    active = models.BooleanField( default=True )
        