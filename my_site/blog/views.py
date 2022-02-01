from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    article_objects = Article.objects.order_by("id").reverse()
    author_objects = Author.objects.all()

    number_of_articles = article_objects.count()
    number_of_authors = author_objects.count()

    return render(request,'blog/index.html',{
        'article_objects' : article_objects,
        'number_of_articles' :number_of_articles,
        'number_of_authors' : number_of_authors,
    })

def load_article(request,slug):
    loaded_article = Article.objects.filter(slug=slug)



    return render(request,'blog/post.html',{
        'loaded_article' : loaded_article,
    })