from image_processing.models import RGBImages, CombinedImage
from rest_framework.serializers import ModelSerializer


class RGBImageSerializer(ModelSerializer):
    class Meta:
        model = RGBImages
        fields = ['image_r', 'image_g', 'image_b']
        extra_kwargs = {
                        'image_r': {'required': True},
                        'image_g': {'required': True},
                        'image_b': {'required': True},
                        }
