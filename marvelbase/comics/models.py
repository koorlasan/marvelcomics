from django.db import models
from django.urls import reverse
import json

# это выводится в панели администратора, надо регистрировать в admin.py
class ComicData(models.Model):
    title = models.CharField(max_length=1024, default=None)
    description = models.TextField(null=True, default=None)
    thumbnail = models.ImageField(null=True, default=None, upload_to='Pictures')
    dates = models.DateField(null=True, default=None)
    #  variants = models.TextField()
    #  ean = models.TextField()
    #    pictures = models.ImageField()
    #    characters = models.TextField()
    #    stories = models.TextField()



