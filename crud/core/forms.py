from django import forms
from .models import MarvelModel


class MarvelForm(forms.ModelForm):
    # name = forms.CharField()
    # heroic = forms.CharField()
    class Meta:
        model = MarvelModel
        fields= ['name','heroic_name']

    