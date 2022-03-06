from django.shortcuts import render
from django.shortcuts import HttpResponse, get_object_or_404
from .models import Article, Author, HeadingArticle
from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    return HttpResponse("news")


def articles(request):
    articles = Article.objects.all()
    articles = Article.objects.order_by('-created_at')
    heading = HeadingArticle.objects.all()
    main_article = Article.main_article
    main_paginator = Paginator(main_article, per_page=3)
    paginator = Paginator(articles, per_page=30)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        "main_article": page_obj.object_list,
        "main_paginator": main_paginator,
        "articles": page_obj.object_list,
        "paginator": paginator,
        "heading": heading,
        "page_number": int(page_number)
    }
    return render(
        request,
        "articles.html",
        context=context
    )



#def main_articles(request):
 #   main_articles = Main_Article.objects.all()
  #  return render(
   #     request,
    #    {"main_article": main_articles}
    #)


def article_page(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug)
    articles = Article.objects.all()
    articles = Article.objects.order_by('-created_at')
    heading = HeadingArticle.objects.all()
    context = {
        "article": article,
        "articles": articles,
        "heading": heading
    }
    return render(request, "article.html", context=context)

def right_panel_article(request):
    articles = Article.objects.all()
    heading = HeadingArticle.objects.all()
    return render(request, "right_panel_articles.html", {"articles": articles, "heading": heading})


def heading_page(request, heading_id):
    article = Article.objects.filter(heading_id=heading_id)
    heading = HeadingArticle.objects.all()
    category = HeadingArticle.objects.get(pk=heading_id)
    return render(request, "headings_page.html", {"article": article, "heading": heading, "category": category})