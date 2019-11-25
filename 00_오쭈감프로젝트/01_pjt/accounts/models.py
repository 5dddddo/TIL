from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import RegexValidator


class MyUser(AbstractUser):
    # member_id = models.CharField(max_length=15, blank=False, unique=True)
    # member_pw = models.CharField(max_length=15, blank=False)
    phone_regex = RegexValidator(
        regex=r'^\d{3}-\d{3,4}-\d{4}$', message="휴대전화 형식은 xxx-xxxx-xxxx입니다.")
    member_tel = models.CharField(
        validators=[phone_regex], max_length=15, blank=False)
    member_emergency = models.CharField(
        validators=[phone_regex], max_length=15, blank=False)
    member_msg = models.CharField(max_length=100, blank=False)
    member_longitude = models.CharField(max_length=20, blank=True)
    member_latitude = models.CharField(max_length=20, blank=True)
