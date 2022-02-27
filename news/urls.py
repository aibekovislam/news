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
from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls import url
from django.views.generic import RedirectView
from django.conf.urls.static import static
from core.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.articles, name="main"),
    path('article/<int:id>/', article_page, name="article"),
    path('article/right-panel-article/', right_panel_article, name="right_panel_articles"),
    path('heading/<int:heading_id>/', heading_page, name="heading"),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicons/favicon.ico', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# businessman 
# Islam123123#