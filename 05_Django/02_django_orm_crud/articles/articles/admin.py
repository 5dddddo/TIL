from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk','title', 'content', 'created_at', 'updated_at',)
    list_display_links = ('content',)
    list_filter = ('created_at',)
    list_editable = ('title',)
    # list_per_page = 2

admin.site.register(Article, ArticleAdmin) 