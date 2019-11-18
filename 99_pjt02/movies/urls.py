from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:movie_pk>/ratings/new/', views.ratings_new, name='ratings_new'),
    path('<int:movie_pk>/ratings/<int:pk>/delete/', views.ratings_delete, name='ratings_delete'),
]
