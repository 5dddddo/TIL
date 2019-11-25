from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('update/', views.update, name='update'),
    path('index/', views.index, name='index'),
    path('password/', views.change_password, name='change_password'),
]
