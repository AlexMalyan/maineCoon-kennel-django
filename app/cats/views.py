from django.shortcuts import render
from .models import *
# from django.http import HttpResponse

menu = [
    "О сайте",
    "Добавить статью",
    "Обратная связь",
    "Войти",
]


def index(request):
    cats_all = Cat.objects.all()
    cats = Cat.objects.filter(gender__exact='F')

    return render(request, 'cats/index.html',  {
        'cats': cats,
        'menu': menu,
        'title': 'Главная'
    })


def about(request):
    return render(request,
                  'cats/about.html',
                  { 'menu': menu, 'title': 'О Сайте'}
                  )
