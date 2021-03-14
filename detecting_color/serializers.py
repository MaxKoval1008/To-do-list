from rest_framework import serializers
from .models import Picture


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id', 'picture_name', 'picture_img')


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ['picture_img']
