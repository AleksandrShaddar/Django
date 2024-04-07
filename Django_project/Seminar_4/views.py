from random import choice, randint
from .forms import GameForm, AuthorForm

from django.shortcuts import render, redirect

from Seminar_2.models import Author


# Create your views here.
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


def all_games(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game_type = form.cleaned_data['game_type']
            num_tries = form.cleaned_data['num_tries']
            if game_type == 'coin':
                return coin(request, num_tries)
            elif game_type == 'cube':
                return cube(request, num_tries)
            else:
                return redirect('number', num_tries)
    else:
        form = GameForm()
    return render(request, 'Seminar_4/all_games.html', {'form': form})


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            biography = form.cleaned_data['biography']
            birthday = form.cleaned_data['birthday']
            author = Author(name=name, lastname=lastname, email=email, biography=biography, birthday=birthday)
            author.save()
            message = 'Автор добавлен в базу'
        else:
            message = 'Некорректные данные'
    else:
        form = AuthorForm()
        message = 'Введите данные'
    return render(request, 'Seminar_4/form.html', {'form': form, 'message': message})
