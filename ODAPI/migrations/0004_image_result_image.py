# Generated by Django 4.1.4 on 2022-12-27 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ODAPI', '0003_alter_image_background_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='result_image',
            field=models.FileField(blank=True, upload_to='uploads/results/'),
        ),
    ]
