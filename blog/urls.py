from django.urls import path

from .views import *


urlpatterns = [
    path('', index),
    path('planets/<some_planet>/', info_about_planets),  # http://127.0.0.1:8000/blog/some_planet
    path('news/', posts_list),  # http://127.0.0.1:8000/blog/some_planet

]