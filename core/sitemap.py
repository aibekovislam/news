from django.contrib.sitemaps import Sitemap
from .models import Article

class AriclesSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.created_at