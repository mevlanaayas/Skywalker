from django.contrib import admin
from django.contrib.auth.models import User
from base.models import Map, Label

admin.site.empty_value_display = 'Yok'


class MapAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'created_by')
    list_display_links = ('name',)


class LabelAdmin(admin.ModelAdmin):
    list_display = ('name', 'map', 'created_at', 'created_by')
    list_display_links = ('name',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'email')
    list_display_links = ('username',)


admin.site.register(Map, MapAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
