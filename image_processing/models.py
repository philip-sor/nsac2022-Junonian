from django.db import models
# from django.dispatch import receiver
# from django.db.models.signals import post_save
#
# from image_processing.editing import ImageEditor
# Create your models here.


def upload_to(instance, filename):
    return f'rgb_images/{filename}'.format(filename=filename)


def upload_to_combined(instance, filename):
    return f'images/{filename}'.format(filename=filename)


class RGBImages(models.Model):
    image_r = models.ImageField(upload_to=upload_to, default='rgb_images/default.png')
    image_g = models.ImageField(upload_to=upload_to, default='rgb_images/default.png')
    image_b = models.ImageField(upload_to=upload_to, default='rgb_images/default.png')
    metadata = models.JSONField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class CombinedImage(models.Model):
    from_images = models.ForeignKey(RGBImages, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to_combined, default='images/default.png')


# @receiver(post_save, sender=RGBImages)
# def rgb_images_create_handler(sender, instance, created, *args, **kwargs):
#     if created:
#         print(instance.image_r)
#         image_editor = ImageEditor(image_r=instance.image_r,
#                                    image_g=instance.image_g,
#                                    image_b=instance.image_b)
#         image_editor.combine_images()
#
