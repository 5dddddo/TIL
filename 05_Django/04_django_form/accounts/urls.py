from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/',views.change_password, name='change_password'),
    path('<str:username>/', views.profile, name='profile'),
]
