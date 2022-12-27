# Generated by Django 4.1.4 on 2022-12-27 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ODAPI', '0002_rename_images_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='background_image',
            field=models.FileField(upload_to='uploads/backgrounds/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='object_image',
            field=models.FileField(upload_to='uploads/objects/'),
        ),
    ]