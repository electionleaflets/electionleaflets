from django.db import models
from legacy.models import Constituency

class Boundary(models.Model):
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
