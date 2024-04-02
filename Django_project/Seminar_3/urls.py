from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('main/', views.main, name='main'),
    path('coin/<int:num>/', views.coin, name='coin'),
    path('cube/<int:num>/', views.cube, name='cube'),
    path('number/<int:num>/', views.number, name='number'),
]