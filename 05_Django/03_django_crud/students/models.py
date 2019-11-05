from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=10)
    major = models.CharField(max_length=40)

    