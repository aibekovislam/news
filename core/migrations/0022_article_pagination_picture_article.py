# Generated by Django 3.1.7 on 2022-03-10 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_article_pagination_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pagination_picture_article',
            field=models.BooleanField(default=False, verbose_name='Новости для вторых страниц с картинками'),
        ),
    ]
