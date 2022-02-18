from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Article, Author, HeadingArticle
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("news")


def articles(request):
    articles = Article.objects.all()
    heading = HeadingArticle.objects.all()
    context = {
        "articles": articles,
        "heading": heading
    }
    return render(
        request,
        "articles.html",
        context=context
    )



def main_articles(request):
    main_articles = Main_Article.objects.all()
    return render(
        request,
        {"main_article": main_articles}
    )


def article_page(request, id):
    article = Article.objects.get(id=id)
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