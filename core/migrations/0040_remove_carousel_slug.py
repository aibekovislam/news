# Generated by Django 3.1.7 on 2022-04-01 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_carousel_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carousel',
            name='slug',
        ),
    ]
