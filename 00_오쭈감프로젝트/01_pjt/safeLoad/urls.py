from django.urls import path
from . import views

app_name = 'safeLoad'
urlpatterns = [
    path('', views.index, name='index'),
]
