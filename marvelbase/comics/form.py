from .models import ComicData
from django import forms


class ComicDataForm(forms.ModelForm):
    class Meta:
        model = ComicData
        fields = ('title', 'description', 'thumbnail', 'dates')
    title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=1024)
    thumbnail = forms.ImageField()
    dates = forms.DateInput()