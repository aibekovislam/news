# Generated by Django 3.1.7 on 2022-03-08 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20220306_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pagination_article',
            field=models.BooleanField(default=False, verbose_name='Текстовые новости на второй странице'),
        ),
    ]