from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse

from .models import Photo
from random import choice
from PIL import Image, ImageOps, ImageFilter
from django.http import Http404

@api_view(['GET'])
def random_image_full(request):
    return create_Repsonse(Image.open(random_Photo()))

@api_view(['GET'])
def image_full(request, name):
    """ Get Full Image by Name """
    return create_Repsonse(Image.open(get_Photo(name)))

@api_view(['GET'])
def image_square(request, width):
    """ Get Random Image as Square """
    return create_Repsonse(square_image(width,Image.open(random_Photo())))

@api_view(['GET'])
def image_square_name(request, width, name):
    """ Get Image by Name as Square """
    return create_Repsonse(square_image(width,Image.open(get_Photo(name))))

@api_view(['GET'])
def image_rectangle(request, width, height):
    """ Get Random Image as Rectangle """
    return create_Repsonse(rectancle_image(width,height,Image.open(random_Photo())))

@api_view(['GET'])
def image_rectangle_name(request, width, height, name):
    """ Get Image by name as Rectangle """
    return create_Repsonse(rectancle_image(width,height,Image.open(get_Photo(name))))

api_view(['GET'])
def get_random_image_category(request,category):
    """ Get Random Image from Category """
    if not (category in dict(Photo.CATEGORY)):
        raise Http404
    return create_Repsonse(Image.open(random_Photo_category(category)))

api_view(['GET'])
def get_random_image_category_square(request,category,width):
    """ Get random Square Image from Category """
    if not (category in dict(Photo.CATEGORY)):
        raise Http404
    return create_Repsonse(square_image(width,Image.open(random_Photo_category(category))))

api_view(['GET'])
def get_random_image_category_size(request,category,width,height):
    """ Get Random Image Rectangle from Category """
    if not (category in dict(Photo.CATEGORY)):
        raise Http404
    return create_Repsonse(rectancle_image(width,height,Image.open(random_Photo_category(category))))

def random_Photo_category(category):
    """ Pick Random photo from Category """
    if not Photo.objects.filter(category=category):
        raise Http404
    else:
        pks = Photo.objects.filter(category=category).values_list('id', flat=True).order_by('id')
        random_pk = choice(pks)
        return Photo.objects.get(id=random_pk).image

def get_Photo(name):
    if not Photo.objects.filter(name=name):
        raise Http404
    else:
        return Photo.objects.get(name=name).image

def random_Photo():
    """Pick a Random Photo"""
    if not Photo.objects.values_list('id', flat=True).order_by('id'):
        raise Http404
    else:
        pks =  Photo.objects.values_list('id', flat=True).order_by('id')
        random_pk = choice(pks)
        return Photo.objects.get(id=random_pk).image

def create_Repsonse(photo):
    """ Create Response """
    response = HttpResponse(content_type="image/png")
    photo.save(response, "PNG")
    return response

def square_image(width,photo):
    """ Resize Image to Square """
    size = (int(width), int(width))
    return ImageOps.fit(photo, size, Image.ANTIALIAS)

def rectancle_image(width,height,photo):
    """ Resize Image to Rectangle """
    size = (int(width), int(height))
    return ImageOps.fit(photo, size, Image.ANTIALIAS)
