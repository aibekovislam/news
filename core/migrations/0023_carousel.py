# Generated by Django 3.1.7 on 2022-03-13 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_article_pagination_picture_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='carousel_image')),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Карусель',
                'verbose_name_plural': 'Карусель',
            },
        ),
    ]
