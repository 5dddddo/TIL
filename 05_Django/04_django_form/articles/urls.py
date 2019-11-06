from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('detail/', views.detail),
    path('create/', views.create),


]
