from django.contrib import admin
from .models import StreetlampKind, Streetlamp, CCTVKind, CCTV
from accounts.models import Profile
from django.contrib.auth.admin import UserAdmin
from accounts.forms import CustomUserChangeForm
# Register your models here.


class StreetlampKindAdmin(admin.ModelAdmin):
    list_display = ('pk', 'STR_RADIUS',)
    list_editable = ('STR_RADIUS',)


class StreetlampAdmin(admin.ModelAdmin):
    list_display = ('pk', 'STR_KIND', 'STR_ADDRESS_NAME',
                    'STR_LONGITUDE', 'STR_LATITUDE',)
    list_editable = ('STR_KIND', 'STR_ADDRESS_NAME',
                     'STR_LONGITUDE', 'STR_LATITUDE',)
    list_filter = ('STR_KIND',)


class CCTVKindAdmin(admin.ModelAdmin):
    list_display = ('pk',  'CCTV_RADIUS',)
    list_editable = ('CCTV_RADIUS',)


class CCTVAdmin(admin.ModelAdmin):
    list_display = ('pk', 'CCTV_KIND', 'CCTV_ADDRESS_NAME',
                    'CCTV_LONGITUDE', 'CCTV_LATITUDE',)
    list_editable = ('CCTV_KIND', 'CCTV_ADDRESS_NAME',
                     'CCTV_LONGITUDE', 'CCTV_LATITUDE',)
    list_filter = ('CCTV_KIND',)


class ProfileAdmin(admin.ModelAdmin):
    form = CustomUserChangeForm
    list_display = ('pk',  'member_tel', 'member_emergency',
                    'member_msg', 'member_longitude', 'member_latitude')
    list_editable = ('member_tel', 'member_emergency',
                     'member_msg', 'member_longitude', 'member_latitude')


admin.site.register(StreetlampKind, StreetlampKindAdmin)
admin.site.register(Streetlamp, StreetlampAdmin)
admin.site.register(CCTVKind, CCTVKindAdmin)
admin.site.register(CCTV, CCTVAdmin)
admin.site.register(Profile, ProfileAdmin)
