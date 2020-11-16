from django.forms import ModelForm, TextInput
from .models import Comic
from django import forms


class ComicInfo(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=1024)
    thumbnail = forms.ImageField()

class ComicData(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=1024)
    thumbnail = forms.ImageField()
    date = forms.DateField()
    pictures = forms.ImageField()
    characters = forms.CharField(max_length=1024)
    stories = forms.CharField(max_length=1024)