from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('<int:article_pk>/',views.detail),
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
]