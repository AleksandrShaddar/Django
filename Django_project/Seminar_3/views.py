from django.shortcuts import render
from random import choice, randint

# Create your views here.


def about(request):
    text = "Немного информации обо мне."
    context = {'info': text,
               'title': 'About'
               }
    return render(request, 'Seminar_3/about.html', context)


def main(request):
    text = "Главная страница."
    context = {'info': text,
               'title': 'Main'
               }
    return render(request, 'Seminar_3/index.html', context)


def coin(request, num):
    result = [choice(['orel', 'reshka']) for _ in range(num)]
    context = {'result': result}
    return render(request, 'Seminar_3/games.html', context)


def cube(request, num):
    result = [randint(1, 6) for _ in range(num)]
    context = {'result': result}
    return render(request, 'Seminar_3/games.html', context)


def number(request, num):
    result = [randint(1, 100) for _ in range(num)]
    context = {'result': result}
    return render(request, 'Seminar_3/games.html', context)