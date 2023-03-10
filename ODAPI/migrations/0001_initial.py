# Generated by Django 4.1.4 on 2022-12-24 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_image', models.ImageField(upload_to='uploads/objects/')),
                ('background_image', models.ImageField(upload_to='uploads/backgrounds/')),
                ('description', models.CharField(max_length=30)),
            ],
        ),
    ]
