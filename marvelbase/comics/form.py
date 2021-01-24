from django.forms import ModelForm, TextInput
from .models import ComicData
from django import forms

class ComicDataForm(forms.Form):
    class Meta:
        model = ComicData
    title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=1024)
    thumbnail = forms.ImageField()
    dates = forms.DateField()
    # pictures = forms.ImageField
    # variants = forms.CharField(max_length=1024)
    #  ean = forms.CharField(max_length=1024)
    # characters = forms.CharField(max_length=1024)
    # stories = forms.CharField(max_length=1024)