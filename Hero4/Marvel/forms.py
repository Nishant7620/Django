from django import forms
from .models import Marvel

class MarvelForm(forms.ModelForm):
    # name = forms.CharField()
    # heroic_name =forms.CharField()
    class Meta:
        model = Marvel

        fields = ['name','heroic_name']