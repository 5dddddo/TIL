
from django.db import models
from django.conf import settings




# Create your models here.


class Hashtag(models.Model):
    content = models.TextField(unique=True)

class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True)#해시태그 안쓴사람도 유효성 통과할 수 있도록

    def __str__(self):
        return f'[{self.pk}] {self.title}'


class Comment(models.Model):
    # Comment -> 이중 1:N 관계 (Article정보, User정보)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at  =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Model Level에서 Metadata 설정 -> 정렬 기능 사용
    class Meta:
        ordering = ['-pk',]

    def __str(self):
        return self.content



