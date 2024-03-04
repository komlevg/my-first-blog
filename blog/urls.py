from django.urls import path

from .views import *


urlpatterns = [
    path('', posts_list),
    #path('news/', posts_list, name='posts_list_url'),  # http://127.0.0.1:8000/blog/news
    path('news/', List_of_Sky_News.as_view(), name='posts_list_url'),  # http://127.0.0.1:8000/blog/news
    path('post/<str:slug>/', posts_detail, name='posts_detail'),  # http://127.0.0.1:8000/blog/post/<str:slug>/
    path('tags/', tags_list, name='tags_list_url'),
    path('tags/<str:slug>/', tag_detail, name='tag_detail_url'),
    path('add/', addpage, name='addpage_url'),
    path('addphoto/', addphoto, name='addphoto_url'),

]