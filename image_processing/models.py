from django.db import models

# Create your models here.


def upload_to(instance, filename):
    return f'rgb_images/{filename}'.format(filename=filename)


def upload_to_combined(instance, filename):
    return f'images/{filename}'.format(filename=filename)


class RGBImages(models.Model):
    image_r = models.ImageField(upload_to=upload_to, default='rgb_images/default.png')
    image_g = models.ImageField(upload_to=upload_to, default='rgb_images/default.png')
    image_b = models.ImageField(upload_to=upload_to, default='rgb_images/default.png')


class CombinedImage(models.Model):
    from_images = models.ForeignKey(RGBImages, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to_combined, default='images/default.png')

