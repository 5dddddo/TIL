from django.contrib import admin
from .models import Streetlamp_Kind, Streetlamp, CCTV_Kind, CCTV
# Register your models here.


class StreetlampKindAdmin(admin.ModelAdmin):
    list_display = ('pk', 'STR_KIND', 'STR_RADIUS',)


class StreetlampAdmin(admin.ModelAdmin):
    list_display = ('pk', 'STR_KIND', 'STR_LONGITUDE', 'STR_LATITUDE',)


class CCTV_KindAdmin(admin.ModelAdmin):
    list_display = ('pk', 'CCTV_KIND', 'CCTV_RADIUS',)


class CCTVAdmin(admin.ModelAdmin):
    list_display = ('pk', 'CCTV_KIND', 'CCTV_LONGITUDE', 'CCTV_LATITUDE',)


admin.site.register(Streetlamp_Kind, StreetlampKindAdmin)
admin.site.register(Streetlamp, StreetlampAdmin)
admin.site.register(CCTV_Kind, CCTV_KindAdmin)
admin.site.register(CCTV, CCTVAdmin)
