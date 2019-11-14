from django.urls import path
from articles import views

app_name = 'articles'
urlpatterns = [
    path('<int:hash_pk>/hashtag/', views.hashtag, name='hashtag'),
    path('explore/', views.explore, name='explore'),
    path('list/', views.list, name='list'),
    path('<int:article_pk>/follow/<int:user_pk>/',views.follow, name="follow"),
    path('<int:article_pk>/like/', views.like, name='like'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:article_pk>/update/', views.update, name='update'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
]
