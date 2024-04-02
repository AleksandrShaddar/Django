from django.shortcuts import render
from django.http import HttpResponse
# import logging
import random
from .models import Games, Author
from datetime import date

# Create your views here.
# logger = logging.basicConfig(__name__)

def game(request):
    side = random.choice(['orel', 'reshka'])
    game = Games(
        side=side,
        )
    game.save()
    return HttpResponse(game)

def statistics(request):
    data = Games.stat_game()
    return HttpResponse(f'{data}')

def create_authors(request):
    result = []
    for i in range(10):
        author = Author(name=f'Name{i}', lastname=f'lastname{i}', email=f'email{i}@mail.ru', biography=f'Biography{i}', birthday=date.today())
        author.save()
        result.append(author.fullname())
    return HttpResponse(f'{result}')