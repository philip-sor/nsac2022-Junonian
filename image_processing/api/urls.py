from django.urls import path
from .views import RGBImageUpload, RGBImageList, CombinedImageList, CombinedImageGet

urlpatterns = [
    path('rgb_add/', RGBImageUpload.as_view(), name='add_rgb'),
    path('rgb_list/', RGBImageList.as_view(), name='list_rgb'),
    path('combined_list/', CombinedImageList.as_view(), name='list_combined_img'),
    path('combined_get/<int:from_images>', CombinedImageGet.as_view(), name='get_combined_img')
    # path('combined_add/', CombinedImageCreate.as_view(), name='add_combined')

]

