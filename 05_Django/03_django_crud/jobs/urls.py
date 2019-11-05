from django.contrib import admin
from django.urls import path,include
from jobs import views

app_name = 'jobs'
urlpatterns = [
    path('', views.index, name='index'),
    path('name/', views.name, name='name'),
]