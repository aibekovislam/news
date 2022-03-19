"""news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cgitb import handler
from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls import url
from django.views.generic import RedirectView
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from core.sitemap import AriclesSitemap 
from core.views import *
from django.views.static import serve


sitemaps = { 
    'articles': AriclesSitemap
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.articles, name="main"),
    path('2/', views.article_page_2, name="article_page_2"),
    path('article/<slug:article_slug>/', article_page, name="article"),
    path('carousel/<int:id>/', carousel_page, name="carousel"),
    path('right-panel-article/', right_panel_article, name="right_panel_articles"),
    path('heading/<int:heading_id>/', heading_page, name="heading"),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots"),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicons/favicon.ico', permanent=True)),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404=HandleNotFound

# businessman 
# Islam123123#