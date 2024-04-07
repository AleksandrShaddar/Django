from django.urls import path
from . import views

urlpatterns = [
    path('coin/<int:num>/', views.coin, name='coin'),
    path('cube/<int:num>/', views.cube, name='cube'),
    path('number/<int:num>/', views.number, name='number'),
    path('all_games/', views.all_games, name='all_games'),
    path('add_author/', views.add_author, name='add_author'),
]
