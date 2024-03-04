from django.http import HttpResponse
from django.shortcuts import render


def check_index(request):
    data = {'sometext': 'наименьшая планета Солнечной системы и самая близкая'}
    return render(request, 'blog/check_index.html', data)