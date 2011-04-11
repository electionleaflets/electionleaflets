from django.contrib     import admin
from leaflets.models import Leaflet, LeafletPartyAttack, LeafletTag, LeafletCategory, LeafletConstituency
from tags.models import Tag

class LeafletTagInline(admin.TabularInline):
    model = LeafletTag

class LeafletCategoryInline(admin.TabularInline):
    model = LeafletCategory

class LeafletPartyAttackInline(admin.TabularInline):
    model = LeafletPartyAttack

class LeafletConstituencyInline(admin.TabularInline):
    model = LeafletConstituency

class LeafletOptions(admin.ModelAdmin):
    list_display         = ['id', 'title', 'publisher_party', 'postcode', 'name', 'email','get_description', 'live']    
    search_fields        = ['title', 'postcode']  
    ordering             = ['title']
    inlines = [ LeafletConstituencyInline, LeafletCategoryInline, LeafletPartyAttackInline] # LeafletTagInline,


    def get_description(self,obj):
        if obj.description:
            return obj.description[0:50]
        return ''
    get_description.short_description = 'Description'
    
    
admin.site.register( Leaflet, LeafletOptions )
