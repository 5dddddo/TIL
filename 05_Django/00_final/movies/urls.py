from django.contrib import admin
from django.urls import path
from movies import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'),
    path('<int:movie_pk>/edit/', views.edit, name='edit'),
    path('<int:movie_pk>/update/', views.update, name='update'),
]