from rest_framework import serializers
from .models import Video,Face

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('url')

class FaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Face
        fields = ('name','img','suspeito')