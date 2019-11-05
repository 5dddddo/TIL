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