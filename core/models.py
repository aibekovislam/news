from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.forms import BooleanField, CharField, ImageField
from django.utils.translation import gettext_lazy as _
from django.shortcuts import reverse



class Article(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    tt = models.CharField(max_length=255, null=True, blank=True, verbose_name="Подтекст")
    text = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True, blank=True)
    author = models.ForeignKey(
        to="Author",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="article",
        verbose_name=_("Автор")
    )
    heading = models.ForeignKey(
        to="HeadingArticle",
        on_delete=models.PROTECT,
        null=True,
        related_name="article",
        verbose_name=_("Рубрика")
    )

    readers = models.ManyToManyField(
        to=User,
        related_name="readed_articles",
        blank=True,
        verbose_name=_("Читатели")
    )

    views = models.IntegerField(default=0, verbose_name=_("Просмотры"))

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )

    main_article = models.BooleanField(default=False, verbose_name=_("Первая новость"))

    text_article = models.BooleanField(default=False, verbose_name=_("Текстовые новости"))

    center_article = models.BooleanField(default=False)

    right_panel_article = models.BooleanField(default=False, verbose_name=_("Главные новости"))

    pagination_article = models.BooleanField(default=False, verbose_name=_("Архивные"))
    
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    metades = models.TextField(null=True, blank=True, verbose_name=_("Ключевые слова"))

    picture = models.ImageField(
        upload_to="articles_image",
        null=True, blank=True,
        verbose_name="Главная картинка статьи"    
    )

    def get_absolute_url(self):
        return reverse("article", kwargs={'article_slug': self.slug})
    

    def __str__(self):
        return self.title


class Author(models.Model):
    user = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True, blank=True)

    def get_absolute_url(self):
        return reverse("author", kwargs={'author_slug': self.slug})

    nik = models.CharField(max_length=55)

    photo = models.ImageField(upload_to="photo", null=True, blank=True)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
    
    def __str__(self):
        return self.nik


class ArticleImage(models.Model):
    img = models.ImageField(upload_to="articles_image")
    article = models.ForeignKey(
        to=Article,
        on_delete=models.CASCADE,
        related_name="images",
    )

class HeadingArticle(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Рубрика"
        verbose_name_plural = "Рубрики"

    def __str__(self):
        return self.title



class Carousel(models.Model):
    picture = models.ImageField(upload_to='carousel_image')
    title = models.CharField(max_length=150)
    text = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )

    def get_absolute_url(self):
        return reverse("article", kwargs={'article_slug': self.slug})
    
    class Meta:
        verbose_name = "Карусель"
        verbose_name_plural = "Карусель"


    def __str__(self):
        return self.title





