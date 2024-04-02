from django.urls import path
from .views import game, statistics, create_authors

urlpatterns = [
    path('game/', game, name='game'),
    path('stat/', statistics, name='statistics'),
    path('authors/', create_authors, name='authors'),
]
