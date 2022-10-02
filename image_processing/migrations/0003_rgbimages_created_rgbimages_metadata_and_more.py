# Generated by Django 4.1.1 on 2022-10-02 07:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('image_processing', '0002_alter_combinedimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='rgbimages',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rgbimages',
            name='metadata',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rgbimages',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
