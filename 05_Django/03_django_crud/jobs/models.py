from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=20)
    past_job = models.CharField(max_length=30)
