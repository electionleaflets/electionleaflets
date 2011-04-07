from django import forms
from leaflets.models import UploadSession

from parties.models import Party
from categories.models import Category
from leaflets.models import Leaflet

class LeafletFileUploadForm( forms.ModelForm ):
    class Meta:
        model = UploadSession
        exclude = ('key',)
        
DELIVERY_CHOICES =     [(0, 'Today'),
    (1, 'Yesterday'),
    (7, 'Last week'),
    (14, 'Couple of weeks ago'),
    (30, 'Last month'),    
    (60, 'Two months ago'),    
    (90, 'Three months ago'),    
]
            
        
class LeafletInfoForm(forms.ModelForm):
    title = forms.CharField( max_length=128,error_messages = {'required': u'Please add a title for this leaflet'} )
    description = forms.CharField( max_length=512, widget=forms.Textarea, required=False)
    postcode = forms.CharField( max_length=20,error_messages = {'required': u'Please add a post code for this leaflet'} )
    publisher_party = forms.ModelChoiceField(queryset=Party.objects.filter(show_on_add_page=True).order_by('-force_top').all(), error_messages = {'required': u'Please specify the party responsible for this leaflet'})
    attacks = forms.ModelMultipleChoiceField( queryset=Party.objects.filter(show_on_add_page=True).order_by('-force_top').all(), widget=forms.CheckboxSelectMultiple, required=False )
    categories = forms.ModelMultipleChoiceField( queryset=Category.objects.order_by('name').all(), widget=forms.CheckboxSelectMultiple, required=False )
    
    date_delivered_text = forms.ChoiceField( choices=DELIVERY_CHOICES, widget=forms.Select() )


    
    tags = forms.CharField( max_length=512, widget=forms.Textarea, required=False)
    name = forms.CharField( max_length=100, error_messages = {'required': u'Please add your name'})
    email = forms.EmailField(error_messages = {'required': u'Please add a valid email address'})

    lat = forms.CharField( max_length=20,widget=forms.HiddenInput() )
    lng = forms.CharField( max_length=20,widget=forms.HiddenInput() )    
    
#    def clean_date_delivered(self):
    
    class Meta:
        model = Leaflet
        exclude = ('date_uploaded', 'date_delivered','constituencies')








