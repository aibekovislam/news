# Generated by Django 3.1.7 on 2022-02-28 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_article_margin_article_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
