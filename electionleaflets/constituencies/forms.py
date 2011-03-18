from django import forms

class ConstituencyLookupForm(forms.Form):
    from constituencies.models import Constituency
    
    search = forms.CharField( required=False )
    constituency = forms.ModelChoiceField( queryset=Constituency.objects.order_by('name').all(), required=False )
