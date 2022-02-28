from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Article


class AriclesSitemap(Sitemap):
    
    def item(self):
        return Article.objects.all()

    def location(self, item):
        return reverse(item)
