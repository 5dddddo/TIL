from django.contrib import admin
from .models import Article, Comment, Hashtag
# Register your models here.


class CommentAdmin(admin.ModelAdmin):


    list_display = ('pk','content','created_at','updated_at',)

class HashTagAdmin(admin.ModelAdmin):

    list_display = ('pk','content',)

# admin.site.register(Article, ArticlesConfig)
admin.site.register(Comment, CommentAdmin)

admin.site.register(Hashtag, HashTagAdmin)