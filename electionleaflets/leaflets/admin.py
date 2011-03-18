"""
Admin for the leaflet, this really does need a lot of inlines for the associated
objects

TODO: Fix up all the required inlines
"""

from django.contrib     import admin
from leaflets.models import Leaflet

class LeafletOptions(admin.ModelAdmin):
    list_display         = [ 'title', 'publisher_party', 'postcode', 'name', 'email','get_description']    
    search_fields        = ['title', 'postcode']  
    ordering             = ['title']

    def get_description(self,obj):
        if obj.description:
            return obj.description[0:50]
        return ''
    get_description.short_description = 'Description'
    
    
admin.site.register( Leaflet, LeafletOptions )
