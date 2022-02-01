from ctypes.wintypes import tagSIZE
from operator import mod
from pyexpat import model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    name = models.CharField(blank=True,default="Unknown User",max_length=100)
    email = models.EmailField(max_length=254,blank=True,default="")

    def __str__(self):
        return f"author name:{self.name} ,author email:{self.email}"

class Article(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(default="image1.jpg")
    slug = models.SlugField(default='',editable=False,max_length=200,db_index=True,unique=True)
    author = models.ForeignKey(Author,default="Unknown User",on_delete=models.SET_DEFAULT)
    # author = models.CharField(blank=True,default="Unknown User",max_length=100) # should be automatic
    content = models.TextField(blank=True,default="")
    # tags and time and imagelink
    
    def get_absolute_url(self):
        return reverse("model_detail", args=[self.slug])
    

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        return super().save(*args,**kwargs)

    def __str__(self):
        return f"article name:{self.title} ,article author: ({self.author})"