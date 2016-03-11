from django.conf.urls import url
from django.contrib import admin
from loremimg.images import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^$', views.random_image_full),
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<name>[a-zA-Z]+)/$', views.image_full),
    url(r'^(?P<width>[0-9]+)/$', views.image_square),
    url(r'^(?P<width>[0-9]+)/(?P<name>[a-zA-Z]+)/$', views.image_square_name),
    url(r'^(?P<width>[0-9]+)/(?P<height>[0-9]+)/$', views.image_rectangle),
    url(r'^(?P<width>[0-9]+)/(?P<height>[0-9]+)/(?P<name>[a-zA-Z]+)/$', views.image_rectangle_name),
    url(r'^category/(?P<category>[a-zA-Z]+)/$', views.get_random_image_category),
    url(r'^category/(?P<category>[a-zA-Z]+)/(?P<width>[0-9]+)/$', views.get_random_image_category_square),
    url(r'^category/(?P<category>[a-zA-Z]+)/(?P<width>[0-9]+)/(?P<height>[0-9]+)/$', views.get_random_image_category_size),
]
