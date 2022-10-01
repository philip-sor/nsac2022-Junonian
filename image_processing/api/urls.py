from django.urls import path
from .views import RGBImageUpload, RGBImageGet

urlpatterns = [
    path('rgb_add/', RGBImageUpload.as_view(), name='add_rgb'),
    path('rgb_get/', RGBImageGet.as_view(), name='get_rgb')

]

