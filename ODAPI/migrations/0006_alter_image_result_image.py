# Generated by Django 4.1.4 on 2022-12-27 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ODAPI', '0005_alter_image_result_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='result_image',
            field=models.FileField(blank=True, upload_to='uploads/results/'),
        ),
    ]
