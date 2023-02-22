from django import forms
from .models import *

class OdamForm(forms.ModelForm):

    class Meta:
        model = Odam
        fields = '__all__'
