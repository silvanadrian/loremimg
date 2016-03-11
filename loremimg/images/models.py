from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Photo(models.Model):
    name = models.CharField(max_length=40, unique=True)
    CATEGORY = (
        ('landscapes', 'Landscapes'),
        ('architecture', 'Architecture'),
        ('people', 'People'),
        ('animals', 'Animals'),
        ('various', 'Various')
    )
    category = models.CharField(max_length=20,choices=CATEGORY,default='various')
    image = models.ImageField(upload_to='images')
