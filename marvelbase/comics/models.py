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

class ComicData(models.Model):
    title = models.CharField(max_length=1024, default=None)
    description = models.TextField(null=True, default=None)
    thumbnail = models.ImageField(null=True, default=None)
  #  variants = models.TextField()
  #  ean = models.TextField()
    dates = models.DateField(null=True, default=None)
 #    pictures = models.ImageField()
 #    characters = models.TextField()
 #    stories = models.TextField()



