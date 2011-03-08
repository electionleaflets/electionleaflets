from django import forms
from leaflets.models import UploadSession

from parties.models import Party
from categories.models import Category

class LeafletFileUploadForm( forms.ModelForm ):
    class Meta:
        model = UploadSession
        exclude = ('key',)
        
class LeafletInfoForm(forms.Form):
    title = forms.CharField( max_length=128 )
    transcript = forms.CharField( max_length=512, widget=forms.Textarea)
    postcode = forms.CharField( max_length=20 )
    party = forms.ModelChoiceField(queryset=Party.objects.order_by('-popular').all())
    parties = forms.ModelMultipleChoiceField( queryset=Party.objects.order_by('-popular').all(), widget=forms.CheckboxSelectMultiple )
    categories = forms.ModelMultipleChoiceField( queryset=Category.objects.order_by('name').all(), widget=forms.CheckboxSelectMultiple )
    
    tags = forms.CharField( max_length=512, widget=forms.Textarea)
    name = forms.CharField( max_length=100)
    email = forms.EmailField()
    
