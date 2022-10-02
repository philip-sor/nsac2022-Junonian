from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import response, status
from .serializers import RGBImageSerializer
from image_processing.models import RGBImages, CombinedImage

from ..editing import ImageEditor

from django.dispatch import receiver
from django.db.models.signals import post_save

from image_processing.editing import ImageEditor

class RGBImageUpload(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = RGBImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            image_editor = ImageEditor(image_r=f"/media/rgb_images/{request.data['image_r']}",
                                       image_g=f"/media/rgb_images/{request.data['image_g']}",
                                       image_b=f"/media/rgb_images/{request.data['image_b']}")
            image_editor.combine_images()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RGBImageGet(generics.ListAPIView):
    serializer_class = RGBImageSerializer

    def get_queryset(self):
        rgb_images = RGBImages.objects.all()
        return rgb_images


@receiver(post_save, sender=RGBImages)
def rgb_images_create_handler(sender, instance, created, *args, **kwargs):
    if created:
        print(instance.image_r)
        image_editor = ImageEditor(image_r=instance.image_r,
                                   image_g=instance.image_g,
                                   image_b=instance.image_b)
        image_editor.combine_images()

