
from django.shortcuts import render, redirect

from blog.models import SkyNews, Tag
from blog.forms import AddPostForm

from django.views.generic import ListView
# Create your views here.


def posts_list(request):
    posts = SkyNews.objects.all()
    return render(request, 'blog/list_of_news.html', context={'posts':posts})

#замена ф-ции posts_list на спец класс
class List_of_Sky_News(ListView):
    model = SkyNews
    template_name = 'blog/list_of_news.html'
    #выбираем название var к которой будем обращаться в html
    context_object_name = 'posts'
    #
    # def get_queryset(self):


def posts_detail(request, slug):
    post = SkyNews.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post':post})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags':tags})


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'blog/tag_detail.html', context={'tag': tag})


def addpage(request):
    print(request)
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts_list_url")
    else:
        form = AddPostForm()

    data = {
        'title': 'добавление новости',
        'form': form
    }
    return render(request, 'blog/addnews.html', data)


def handle_uploaded_file(f):
    with open(f'uploads/{f.name}', "wb+") as destination:
        for piece in f.chunks():
            destination.write(piece)

# def addphoto(request):
#     if request.method == 'POST':
#         handle_uploaded_file(request.FILES['file_upload'])
#     return render(request, 'blog/addphoto.html')

def addphoto(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("posts_list_url")
    else:
        form = AddPostForm()

    data = {
        'title': 'добавление новости с фото',
        'form': form
    }
    return render(request, 'blog/addphoto.html', data)
