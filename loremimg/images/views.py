from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse

from .models import Photo
from random import choice
from serializers import PhotoSerializer
from PIL import Image, ImageOps, ImageFilter

@api_view(['GET'])
def image_full(request, name):
    """
    Get Full Image by Name
    """
    photo = Image.open(random_Photo())
    response = HttpResponse(content_type="image/png")
    photo.save(response, "PNG")
    return response

@api_view(['GET'])
def image_square(request, width):
    """
    Get Random Image as Square
    """
    size = (int(width), int(width))
    photo = Image.open(random_Photo())
    thumb = ImageOps.fit(photo, size, Image.ANTIALIAS)
    response = HttpResponse(content_type="image/png")
    thumb.save(response, "PNG")
    return response

@api_view(['GET'])
def image_square_name(request, width, name):
    """
    Get Image by Name as Square
    """
    size = (int(width), int(width))
    photo = Image.open(Photo.objects.get(name=name).image)
    thumb = ImageOps.fit(photo, size, Image.ANTIALIAS)
    response = HttpResponse(content_type="image/png")
    thumb.save(response, "PNG")
    return response

@api_view(['GET'])
def image_rectangle(request, width, height):
    """
    Get Random Image as Rectangle
    """
    size = (int(width), int(height))
    photo = Image.open(random_Photo())
    thumb = ImageOps.fit(photo, size, Image.ANTIALIAS)
    response = HttpResponse(content_type="image/png")
    thumb.save(response, "PNG")
    return response

@api_view(['GET'])
def image_rectangle_name(request, width, height, name):
    """
    Get Image by name as Rectangle
    """
    size = (int(width), int(height))
    photo = Image.open(Photo.objects.get(name=name).image)
    thumb = ImageOps.fit(photo, size, Image.ANTIALIAS)
    response = HttpResponse(content_type="image/png")
    thumb.save(response, "PNG")
    return response


def random_Photo():
    """Pick a Random Photo"""
    pks =  Photo.objects.values_list('id', flat=True).order_by('id')
    random_pk = choice(pks)
    return Photo.objects.get(id=random_pk).image
