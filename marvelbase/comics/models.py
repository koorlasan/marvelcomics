from django.db import models
from django.urls import reverse
from .filling import *
import json
from .apikey import *

# это выводится в панели администратора, надо регистрировать в admin.py
class Comic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField()
    date = models.DateField()


    def __unicode__(self):
        return self.title


    def get_absolute_url(self):
         return ('views.show_results', [str(self.title)])

class ComicData(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField()
    date = models.DateField()
    pictures = models.ImageField()
    characters = models.TextField()
    stories = models.TextField()

def get_absolute_url(self):
    return reverse('show-results', args=[str(self.title)])
def __unicode__(self):
    return self.title

# Create your models here.
