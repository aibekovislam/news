# Generated by Django 3.1.7 on 2022-04-01 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_article_metades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='metades',
            field=models.TextField(blank=True, null=True, verbose_name='Ключевые слова'),
        ),
    ]
