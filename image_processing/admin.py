from django.contrib import admin
from image_processing.models import RGBImages, CombinedImage

# Register your models here.

admin.site.register(RGBImages)
admin.site.register(CombinedImage)
