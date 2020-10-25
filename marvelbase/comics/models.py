from django.db import models
from .filling import *
import json
from .apikey import *


class Comic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField()

#    def __unicode__(self):
#        return self.title

# Create your models here.
#title = json.models.CharField(max_length=255)
