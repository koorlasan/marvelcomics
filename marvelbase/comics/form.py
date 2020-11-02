from django.forms import ModelForm, TextInput
from .models import Comic
from django import forms


class ComicInfo(forms.Form):
    # title = forms.CharField(max_length=255, source=Comic.title)
    # description = forms.TextField(source=Comic.description)
    # thumbnail = forms.ImageField(source=Comic.thumbnail)
    title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=1024)
    thumbnail = forms.ImageField()


