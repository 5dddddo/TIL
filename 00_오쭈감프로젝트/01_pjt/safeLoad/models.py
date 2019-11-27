from django.db import models
from django.conf import settings
# Create your models here.


class StreetlampKind(models.Model):
    # STR_KIND = models.CharField(max_length=15, unique=True)
    STR_RADIUS = models.CharField(max_length=15, unique=True)

    class Meta:
        ordering = ['pk', ]

    def __str__(self):
        return f'{self.pk}'


# class Streetlamp(models.Model):
#     STR_ADDRESS_NAME = models.CharField(max_length=50)
#     STR_KIND = models.ForeignKey(StreetlampKind, on_delete=models.CASCADE)
#     STR_LONGITUDE = models.CharField(max_length=20)
#     STR_LATITUDE = models.CharField(max_length=20)

#     class Meta:
#         ordering = ['pk', ]

#     def __str__(self):
#         return f'{self.pk}'


class CCTVKind(models.Model):
    # CCTV_KIND = models.CharField(max_length=15, unique=True)
    CCTV_RADIUS = models.CharField(max_length=15, unique=True)

    class Meta:
        ordering = ['pk', ]

    def __str__(self):
        return f'{self.pk}'


class CCTV(models.Model):
    CCTV_ADDRESS_NAME = models.CharField(max_length=50)
    CCTV_KIND = models.ForeignKey(CCTVKind, on_delete=models.CASCADE)
    CCTV_LONGITUDE = models.CharField(max_length=20)
    CCTV_LATITUDE = models.CharField(max_length=20)

    class Meta:
        ordering = ['pk', ]

    def __str__(self):
        return f'{self.pk}'
