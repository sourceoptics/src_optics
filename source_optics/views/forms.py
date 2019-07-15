# contributor note: the django UI will be eventually replaced by a new dynamic frontend speaking to the REST API, do not add features

from django import forms
from ..models import *

class RepositoryForm(forms.Form):
    organization = forms.ModelChoiceField(queryset = Organization.objects.all(), required = True)
    credential = forms.ModelChoiceField(queryset = LoginCredential.objects.all(), required=False )    
    enabled = forms.BooleanField(required = True)
    url = forms.CharField(max_length=100, required = True)
    name = forms.CharField(max_length=100, required = True)
