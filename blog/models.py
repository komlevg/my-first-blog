from django.db import models
from django.urls import reverse

# Create your models here.
'''
from django.db import models: This imports the 'models' module from Django's database package.
 Models define how data is stored and retrieved from databases.
from django.urls import reverse: Imports the 'reverse' function which allows you to generate URLs by reversing the URL 
patterns. It's useful when you want to create links without hardcoding the URL.
# Create your models here.: This is just a comment indicating where you should 
start defining your models. In this case, there's already one model defined called 'SkyNews'.
class SkyNews(models.Model): Defines a new model named 'SkyNews', inheriting from Django's built-in Model class.
Here's what each field within the 'SkyNews' model means:
title = models.CharField(max_length=255, verbose_name="Заголовок"): Creates a character (string) field for storing
titles up to 255 characters long. The 'verbose_name' argument provides a human-readable name for the field.
slug = models.SlugField(max_length=255, db_index=True, unique=True): A slug is a short label for something, 
containing only letters, numbers, underscores, or hyphens. Slugs are generally used in URLs. Setting 'unique=True' ensures 
that no two objects have the same slug. By setting 'db_index=True', you tell Django to index this column in the database,
 making queries faster.
newscontent = models.TextField(blank=True): Creates a text field for longer pieces of content like articles or blog posts.
 Since 'blank=True', empty submissions are allowed.
time_create = models.DateTimeField(auto_now_add=True): Stores datetime information about when an object was created.
 With 'auto_now_add=True', the current date and time get automatically assigned whenever a new instance of the model
  gets saved.
time_update = models.DateTimeField(auto_now=True): Similar to 'time_created', but updates every time the object is modified
 instead of using the initial creation time.
is_published = models.BooleanField(default=True): Represents whether the article is published ('True') or not ('False').
'''
class SkyNews(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")#строковое поле с ограничением кол-ва ввода
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    newscontent = models.TextField(blank=True)#бланк тру - можно ниче не передавать
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    #new - photo for news
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default=None, blank=True, null=True, verbose_name='фото')

    ''' This is a Python function that returns the absolute URL for a specific object instance in Django 
   web framework. It uses the reverse function from django.urls module to generate the URL by 
   reversing the URL configuration. In this case, it reverses the 'posts_detail' view name and
    passes the keyword argument 'slug' with the value of the current object's slug attribute (self.slug).
     This method is commonly used in class-based 
   views (CBV) when you need to create links to detail pages for individual objects.'''
    def get_absolute_url(self):
        return reverse('posts_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]


class Tag(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name="название тэга")#строковое поле с ограничением кол-ва ввода
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})


