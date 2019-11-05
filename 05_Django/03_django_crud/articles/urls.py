from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),      # READ Logic - Index
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete', views.comments_delete, name='comments_delete'),
    # path('new/', views.new, name='new'),        # CREATE Logic - 사용자에게 폼 전달
    path('create/', views.create, name='create'),  # CREATE Logic  데이터베이스에 저장  GET(new) / POST(create)
    path('<int:article_pk>/', views.detail, name='detail'),    # READ Logic - Deatil
    path('<int:article_pk>/delete/', views.delete, name='delete'),      # DELETE Logic
    # path('<int:article_pk>/edit/', views.edit, name='edit'),     # UPDATE Logic - 폼 전달
    path('<int:article_pk>/update/' , views.update, name='update'), #GET(edit) / POST(update)
