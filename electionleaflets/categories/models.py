from django.db import models
from core.util import AutoSlugField

class Category(models.Model):
    name = models.CharField(max_length=765)
    description = models.TextField(blank=True)
    default_value = models.IntegerField(null=True, blank=True)
    slug = AutoSlugField( populate_from='name', max_length=255)
    class Meta:
        db_table = u'category'

    def __unicode__(self):
        return self.name