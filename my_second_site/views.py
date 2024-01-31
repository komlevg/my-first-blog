from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    data = {'sometext': 'наименьшая планета Солнечной системы и самая близкая'}
    return render(request, 'blog/index.html', data)