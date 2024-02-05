from django import forms

class Dc(forms.Form):
    name = forms.CharField(label='Full Name')
    heroic_name = forms.CharField()
    