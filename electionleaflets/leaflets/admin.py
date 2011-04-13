from django.contrib     import admin
from leaflets.models import Leaflet, LeafletPartyAttack, LeafletTag, LeafletCategory, LeafletConstituency, LeafletImage
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

class LeafletImageOptions(admin.ModelAdmin):
    list_display         = ['id', 'get_leaflet_title', 'thumbnail']    
    raw_id_fields = ['leaflet']
    
    def get_leaflet_title(self,obj):
        if obj.leaflet:
            return obj.leaflet.title
        return ''
    get_leaflet_title.short_description = 'Leaflet title'
    def thumbnail(self,obj):
        # TODO: This could be where to put the rotate icons and links
        
        return '<img src="%s"/>' % obj.get_small()
    thumbnail.short_description = 'Thumbnail'
    thumbnail.allow_tags = True
    
admin.site.register( LeafletImage, LeafletImageOptions )
