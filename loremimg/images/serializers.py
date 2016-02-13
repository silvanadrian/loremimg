from rest_framework import serializers
from .models import Photo

class PhotoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=40)
    category = serializers.CharField(max_length=20)
    image = serializers.ImageField()
    class Meta:
        model = Photo
        fields = ('name','category','image')
