from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Photo(models.Model):
    name = models.CharField(max_length=40, unique=True)
    CATEGORY = (
        ('LANDSCAPES', 'Landscapes'),
        ('ARCHITECTURE', 'Architecture'),
        ('PEOPLE', 'People'),
        ('ANIMALS', 'Animals'),
        ('VARIOUS', 'Various')
    )
    category = models.CharField(max_length=20,choices=CATEGORY,default='VARIOUS')
    image = models.ImageField(upload_to='images')
