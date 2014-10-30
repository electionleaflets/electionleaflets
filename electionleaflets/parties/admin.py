from django.contrib     import admin
from parties.models import Party

class PartyOptions(admin.ModelAdmin):
    list_display         = [ 'name', 'country', 'slug', 'count', 'popular']    
    search_fields        = ['name']  
    ordering             = ['-popular','name']
    
admin.site.register( Party, PartyOptions )

