# Generated by Django 3.1.7 on 2022-02-28 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_article_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
    ]