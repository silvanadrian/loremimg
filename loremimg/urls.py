from django.conf.urls import url
from django.contrib import admin
from loremimg.images import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<name>[a-zA-Z]+)/$', views.image_full),
    url(r'^(?P<width>[0-9]+)/$', views.image_square),
    url(r'^(?P<width>[0-9]+)/(?P<name>[a-zA-Z]+)/$', views.image_square_name),
    url(r'^(?P<width>[0-9]+)/(?P<height>[0-9]+)/$', views.image_rectangle),
    url(r'^(?P<width>[0-9]+)/(?P<height>[0-9]+)/(?P<name>[a-zA-Z]+)/$', views.image_rectangle_name),
]
