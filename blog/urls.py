from django.urls import path

from .views import *


urlpatterns = [
    path('', index),
    path('planets/<some_planet>/', info_about_planets),  # http://127.0.0.1:8000/blog/some_planet
    path('news/', posts_list, name='posts_list_url'),  # http://127.0.0.1:8000/blog/news
    path('post/<str:slug>/', posts_detail, name='posts_detail'),  # http://127.0.0.1:8000/blog/post/<str:slug>/
    path('tags/', tags_list, name='tags_list_url'),
    path('tags/<str:slug>/', tag_detail, name='tag_detail_url'),
]