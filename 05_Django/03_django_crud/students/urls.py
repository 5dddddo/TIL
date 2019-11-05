from django.contrib import admin
from django.urls import path,include
from students import views

app_name = 'students'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:student_pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:student_pk>/delete/', views.delete, name='delete'),
    path('<int:student_pk>/edit/', views.edit, name='edit'),
    path('<int:student_pk>/update/', views.update, name='update'),
]