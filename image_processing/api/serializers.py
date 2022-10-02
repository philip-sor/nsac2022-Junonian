from image_processing.models import RGBImages, CombinedImage
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from ..editing import ImageEditor


class RGBImageSerializer(ModelSerializer):
    class Meta:
        model = RGBImages
        # fields = ['image_r', 'image_g', 'image_b']
        fields = '__all__'
        extra_kwargs = {
                        'image_r': {'required': True},
                        'image_g': {'required': True},
                        'image_b': {'required': True},
                        }


class CombinedImageSerializer(ModelSerializer):
    class Meta:
        model = CombinedImage
        fields = '__all__'

