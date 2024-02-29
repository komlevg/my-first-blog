
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from blog.models import SkyNews, Tag
from blog.forms import AddPostForm

#from .models import SkyNews

# Create your views here.

# planet_dict = {
#     'mercury': 'наименьшая планета Солнечной системы и самая близкая к Солнцу. Названа в честь древнеримского бога торговли — быстрого Меркурия, поскольку она движется по небу быстрее других планет. Её период обращения вокруг Солнца составляет всего 87,97 земных суток — самый короткий среди всех планет Солнечной системы.',
#     'venus': 'вторая по удалённости от Солнца и шестая по размеру планета Солнечной системы, наряду с Меркурием, Землёй и Марсом принадлежащая к семейству планет земной группы. Названа в честь древнеримской богини любви Венеры.'
# }

planet_dict = [
    {'id': 1, 'title':'mercury',
     'content':'наименьшая планета Солнечной системы и самая близкая к Солнцу. Названа в честь древнеримского бога торговли — быстрого Меркурия, поскольку она движется по небу быстрее других планет. Её период обращения вокруг Солнца составляет всего 87,97 земных суток — самый короткий среди всех планет Солнечной системы.',
     'is_published': True},
    {'id': 2, 'title': 'venus',
     'content': 'вторая по удалённости от Солнца и шестая по размеру планета Солнечной системы, наряду с Меркурием, Землёй и Марсом принадлежащая к семейству планет земной группы. Названа в честь древнеримской богини любви Венеры.',
     'is_published': True,
     'news':'Как показал анализ данных космического аппарата "Венера-Экспресс", в период с 2006 по 2012 год средняя скорость ветров на планете возросла на 33 процента - примерно с 300 км/ч до 400 км/ч, сообщает Space.com. По словам ученых, это очень высокий рост, учитывая и без того бешеную скорость венерианского ветра.'
     },
    {'id': 3, 'title': 'earth',
     'content': 'третья по удалённости от Солнца планета Солнечной системы. Самая плотная, пятая по диаметру и массе среди всех планет Солнечной системы и крупнейшая среди планет земной группы, в которую входят также Меркурий, Венера и Марс',
     'is_published': True},
    {'id': 4, 'title': 'mars',
     'content': 'принадлежащая к семейству планет земной группы.',
     'is_published': True,
     'news':'''Планетологи обнаружили признаки существования на Марсе активного плюма — поднимающейся из мантии струи вещества под равниной Элизий.
На Земле над такими плюмами могут формироваться супервулканы.
Основываясь на геофизической модели, на топографии кратеров и сейсмических данных,
ученые оценили диаметр головы плюма в четыре тысячи километров — примерно такие же размеры
у земных плюмов, говорится в статье, опубликованной в журнале Nature Astronomy.'''
     },
]


def index(request):
    data = {'sometext': 'наименьшая планета Солнечной системы и самая близкая',
            'posts': planet_dict,}
    return render(request, 'blog/check_index.html', data)

def posts_list(request):
    posts = SkyNews.objects.all()
    return render(request, 'blog/index.html', context={'posts':posts})

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


def info_about_planets(request, some_planet):
    descr = planet_dict.get(some_planet)
    data = {'sometext': descr}
    return render(request, 'blog/index.html', data)

# def info_about_planets(request, some_planet):
#     descr = planet_dict.get(some_planet)
#     if descr:
#         return HttpResponse(descr)
#     else:
#         return HttpResponseNotFound(f'не слышал про такую планету - {some_planet}')

    # if some_planet == 'mercury':
    #     return HttpResponse(f'<h1>Статьи по категориям</h1><p>Мерку́рий — наименьшая планета Солнечной системы и самая близкая к Солнцу.'
    #                         f' Названа в честь древнеримского бога торговли — быстрого Меркурия, поскольку она движется по небу быстрее других планет.'
    #                         f' Её период обращения вокруг Солнца составляет всего 87,97 земных суток — самый короткий среди всех планет Солнечной системы.</p>')
    # elif some_planet == 'venus':
    #     return HttpResponse(r"<h1>Статьи по категориям</h1><p>Venus is the second planet from the Sun. "
    #                         r"It is a rocky planet with the densest atmosphere of all the rocky bodies in the Solar System,"
    #                         r" and the only one with a mass and size that is close to that of its orbital neighbour Earth. "
    #                         r"Orbiting inferiorly (inside of Earth's orbit), it appears in Earth's sky always close to the Sun,"
    #                         r" as either a morning star or an evening star")
















