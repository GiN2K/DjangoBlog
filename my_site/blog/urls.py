from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('tags/<str:tag>', views.load_tag_page,name="tags-page"),
    path('posts/<slug:slug>', views.load_article, name="post-page"),
]