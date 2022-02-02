from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
article_objects = Article.objects.order_by("id").reverse()
author_objects = Author.objects.all()

number_of_articles = article_objects.count()
number_of_authors = author_objects.count()

tag_list = Tag.objects.all()
number_of_tags = tag_list.count()

def home(request):
    

    return render(request,'blog/index.html',{
        'article_objects' : article_objects,
        'number_of_articles' :number_of_articles,
        'number_of_authors' : number_of_authors,
        'tag_list' : tag_list,
        'number_of_tags' : number_of_tags,
    })

def load_article(request,slug):
    loaded_article = Article.objects.filter(slug=slug)


    loaded_article_tags = loaded_article[0].tags.all()


    return render(request,'blog/post.html',{
        'loaded_article' : loaded_article,
        'number_of_articles' :number_of_articles,
        'number_of_authors' : number_of_authors,
        'tag_list' : tag_list,
                'number_of_tags' : number_of_tags,
                'loaded_article_tags' : loaded_article_tags,
    })

def load_tag_page(request,tag):
    article_bytag = Article.objects.filter(tags__caption__startswith=tag).order_by("id").reverse()
    
    #loaded_article = Article.objects.filter(tags=tag)
    return render(request,'blog/index.html',{
        'article_objects' : article_bytag,
        'number_of_articles' :number_of_articles,
        'number_of_authors' : number_of_authors,
        'tag_list' : tag_list,
        'number_of_tags' : number_of_tags,
    })
