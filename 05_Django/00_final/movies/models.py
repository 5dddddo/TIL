from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=30)
    title_en = models.CharField(max_length=40)
    audience = models.IntegerField(default=0)
    # open_date = models.DateTimeField(auto_now_add=True)
    open_date = models.TextField()
    genre = models.CharField(max_length=20)
    watch_grade = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

class Comment(models.Model):
    # related_name : 부모 테이블에서 역으로 참조할 때 기본적으로 모델이름_set 형식으로 불러온다.
    # related_name 이라는 값을 설정해서 _set 명령어를 임의로 변경 할 수 있다.
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Model Level에서 Metadata 설정
    class Meta:
        ordering = ['-pk',]

    def __str__(self):
        return self.content