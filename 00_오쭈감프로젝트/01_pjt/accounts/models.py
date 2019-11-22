from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    member_tel = models.CharField(max_length=15, blank=False)
    member_emergency = models.CharField(max_length=15, blank=False)
    member_msg = models.CharField(max_length=100, blank=False)
    member_longitude = models.CharField(max_length=20, blank=True)
    member_latitude = models.CharField(max_length=20, blank=True)
