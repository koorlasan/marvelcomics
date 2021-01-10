from django.forms import ModelForm, TextInput
from .models import ComicData, Comic
from django import forms


class ComicInfoForm(forms.Form):
    class Meta:
        model = Comic
    title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=1024)
    thumbnail = forms.ImageField()

class ComicDataForm(forms.Form):
    class Meta:
        model = ComicData
    title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=1024)
    thumbnail = forms.ImageField()
    variants = forms.CharField(max_length=1024)
    ean = forms.CharField(max_length=1024)
    dates = forms.DateField()
    pictures = forms.ImageField()
    characters = forms.CharField(max_length=1024)
    stories = forms.CharField(max_length=1024)