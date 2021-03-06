from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import HttpResponse, get_object_or_404
from .models import *
from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# importing models and libraries
from django.views import generic
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.views.generic.list import ListView
 


def post(request):
    pass 
# class based view for each post in amp template
def amp(request, article_slug):
        article = get_object_or_404(Article, slug=article_slug)
        articles = Article.objects.all()
        heading = HeadingArticle.objects.all()
        articles = Article.objects.order_by('-created_at')
        context = {
            "articles": articles,
            "article": article,
            "heading": heading
            }
        return render(request, 'amp.html', context=context)


# Create your views here.
def index(request):
    return HttpResponse("news")



def home(request,type, article_slug):
    if(type=='amp'):
        article = get_object_or_404(Article, slug=article_slug)
        articles = Article.objects.all()
        heading = HeadingArticle.objects.all()
        context = {
        "articles": articles,
        "article": article,
        "heading": heading
        }
        return render(request, '.amp.html', context=context)  


def articles(request):
    articles = Article.objects.all()
    articles = Article.objects.order_by('-created_at')
    obj = Carousel.objects.all()
    heading = HeadingArticle.objects.all()
    context = {
        "articles": articles,
        "heading": heading,
        "obj": obj
    }
    return render(
        request,
        "articles.html",
        context=context
    )

def article_page_2(request):
    articles = Article.objects.all()
    articles = Article.objects.order_by('-created_at')
    heading = HeadingArticle.objects.all()
    paginator = Paginator(articles, per_page=30)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "articles": page_obj.object_list,
        "paginator": paginator,
        "heading": heading,
        "page_number": int(page_number)
    }
    return render(request, "articles2.html", context=context)



def HandleNotFound(request, exception):
    articles = Article.objects.all()
    heading = HeadingArticle.objects.all()
    context={
        "articles": articles,
        "heading": heading
    }
    return render(request, "404.html", context=context, status=404)
    

#def main_articles(request):
 #   main_articles = Main_Article.objects.all()
  #  return render(
   #     request,
    #    {"main_article": main_articles}
    #)

#class PostView(ListView):
#     model = Article
#     paginate_by = 5
#     context_object_name = 'articles'
#     template_name = 'test.html'
#     ordering = ['title']


def article_page(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug)
    author = Author.objects.all()
    articles = Article.objects.all()
    obj = Carousel.objects.all()
    articles = Article.objects.order_by('-created_at')
    heading = HeadingArticle.objects.all()
    context = {
        "obj": obj,
        "article": article,
        "articles": articles,
        "heading": heading,
        "author": author
    }
    return render(request, "article.html", context=context)


def author_page(request, author_slug):
    author = get_object_or_404(Author, slug=author_slug)
    return render(request, "author.html", {"author": author})


def carousel_page(request, id):
    carousel = get_object_or_404(Carousel, id=id)
    articles = Article.objects.all()
    articles = Article.objects.order_by('-created_at')
    heading = HeadingArticle.objects.all()
    context = {
        "carousel": carousel,
        "articles": articles,
        "heading": heading
    }
    return render(request, "carousel.html", context=context)

def right_panel_article(request):
    articles = Article.objects.all()
    heading = HeadingArticle.objects.all()
    return render(request, "right_panel_articles.html", {"articles": articles, "heading": heading})


def heading_page(request, heading_id):
    article = Article.objects.filter(heading_id=heading_id)
    heading = HeadingArticle.objects.all()
    category = HeadingArticle.objects.get(pk=heading_id)
    return render(request, "headings_page.html", {"article": article, "heading": heading, "category": category})


