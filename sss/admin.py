from django.contrib.gis import admin
from sss import models


@admin.register(models.District)
class DistrictAdmin(admin.ModelAdmin):
    raw_id_fields = ('region',)

@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'region', 'district', 'created')
    raw_id_fields = ('user', 'region', 'district')
    readonly_fields = ['created',]

@admin.register(models.ProxyCache)
class ProxyCacheAdmin(admin.ModelAdmin):
    list_display = ('id', 'layer_name', 'created', 'active')
    readonly_fields = ['created',]

admin.site.register(models.Region)

