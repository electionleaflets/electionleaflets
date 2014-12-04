from django.contrib     import admin
from boundaries.models import Boundary

class BoundaryOptions(admin.ModelAdmin):
    list_display         = [ 'constituency', 'north', 'south', 'east', 'west']    
    search_fields        = ['constituency__name']  
    ordering             = ['constituency__name']
    
admin.site.register( Boundary,BoundaryOptions )

