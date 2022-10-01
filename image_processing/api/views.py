from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import response, status
from .serializers import RGBImageSerializer
from image_processing.models import RGBImages, CombinedImage


class RGBImageUpload(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = RGBImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RGBImageGet(generics.ListAPIView):
    serializer_class = RGBImageSerializer

    def get_queryset(self):
        rgb_images = RGBImages.objects.all()
        return rgb_images

