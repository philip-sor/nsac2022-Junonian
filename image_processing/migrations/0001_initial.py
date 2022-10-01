# Generated by Django 4.1.1 on 2022-09-30 13:20

from django.db import migrations, models
import django.db.models.deletion
import image_processing.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RGBImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_r', models.ImageField(default='rgb_images/default.png', upload_to=image_processing.models.upload_to)),
                ('image_g', models.ImageField(default='rgb_images/default.png', upload_to=image_processing.models.upload_to)),
                ('image_b', models.ImageField(default='rgb_images/default.png', upload_to=image_processing.models.upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='CombinedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='images/default.png', upload_to='')),
                ('from_images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image_processing.rgbimages')),
            ],
        ),
    ]