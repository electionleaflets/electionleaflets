from django import forms
from leaflets.models import UploadSession

from parties.models import Party
from categories.models import Category
from leaflets.models import Leaflet

class LeafletFileUploadForm( forms.ModelForm ):
    class Meta:
        model = UploadSession
        exclude = ('key',)
        
class LeafletInfoForm(forms.ModelForm):
    title = forms.CharField( max_length=128,error_messages = {'required': u'Please add a title for this leaflet'} )
    transcript = forms.CharField( max_length=512, widget=forms.Textarea, required=False)
    postcode = forms.CharField( max_length=20,error_messages = {'required': u'Please add a post code for this leaflet'} )
    publisher_party = forms.ModelChoiceField(queryset=Party.objects.order_by('-popular').all(), error_messages = {'required': u'Please specify the party responsible for this leaflet'})
    attacks = forms.ModelMultipleChoiceField( queryset=Party.objects.order_by('-popular').all(), widget=forms.CheckboxSelectMultiple, required=False )
    categories = forms.ModelMultipleChoiceField( queryset=Category.objects.order_by('name').all(), widget=forms.CheckboxSelectMultiple, required=False )
    
    tags = forms.CharField( max_length=512, widget=forms.Textarea, required=False)
    name = forms.CharField( max_length=100, error_messages = {'required': u'Please add your name'})
    email = forms.EmailField(error_messages = {'required': u'Please add a valid email address'})
    
    class Meta:
        model = Leaflet
        exclude = ('lat','lng','date_uploaded', 'date_delivered', 'constituencies')








