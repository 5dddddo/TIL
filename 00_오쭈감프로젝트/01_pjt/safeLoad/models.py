from django.db import models
from django.conf import settings
# Create your models here.


class Streetlamp_Kind(models.Model):
    # STR_KIND = models.CharField(max_length=15, unique=True)
    STR_RADIUS = models.CharField(max_length=15, unique=True)

    class Meta:
        ordering = ['-pk', ]

    def __str__(self):
        return f'{self.pk}'


class Streetlamp(models.Model):
    STR_KIND = models.ForeignKey(Streetlamp_Kind, on_delete=models.CASCADE)
    STR_LONGITUDE = models.CharField(max_length=20)
    STR_LATITUDE = models.CharField(max_length=20)

    class Meta:
        ordering = ['-pk', ]

    def __str__(self):
        return f'{self.pk}'


class CCTV_Kind(models.Model):
    # CCTV_KIND = models.CharField(max_length=15, unique=True)
    CCTV_RADIUS = models.CharField(max_length=15, unique=True)

    class Meta:
        ordering = ['-pk', ]

    def __str__(self):
        return f'{self.pk}'


class CCTV(models.Model):
    CCTV_KIND = models.ForeignKey(CCTV_Kind, on_delete=models.CASCADE)
    CCTV_LONGITUDE = models.CharField(max_length=20)
    CCTV_LATITUDE = models.CharField(max_length=20)

    class Meta:
        ordering = ['-pk', ]

    def __str__(self):
        return f'{self.pk}'
