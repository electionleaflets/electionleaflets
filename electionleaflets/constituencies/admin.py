from django.contrib     import admin
from constituencies.models import Constituency, ConstituencyType

class ConstituencyOptions(admin.ModelAdmin):
    list_display         = [ 'name', 'slug','constituency_type']    
    search_fields        = ['name']  
    ordering             = ['name']
    
class ConstituencyTypeOptions(admin.ModelAdmin):
    list_display         = [ 'name', 'country']    
    search_fields        = ['name']  

    
admin.site.register( Constituency, ConstituencyOptions )
admin.site.register( ConstituencyType, ConstituencyTypeOptions )




