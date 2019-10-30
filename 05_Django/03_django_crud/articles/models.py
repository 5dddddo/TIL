from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField( max_length=40)
    content =models.TextField()
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    # 객체 표시 형식 수정
    def __str__(self):
        return f'[{self.pk}] {self.title}'