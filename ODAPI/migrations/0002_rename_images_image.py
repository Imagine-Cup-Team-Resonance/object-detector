# Generated by Django 4.1.4 on 2022-12-24 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ODAPI', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='images',
            new_name='image',
        ),
    ]