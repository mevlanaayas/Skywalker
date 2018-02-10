from django.contrib import admin

# Register your models here.
from base.models import CustomUser, Map, Label

admin.site.empty_value_display = 'Yok'


class MapAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'created_by')
    list_display_links = ('name',)


class LabelAdmin(admin.ModelAdmin):
    list_display = ('name', 'map', 'created_at', 'created_by')
    list_display_links = ('name',)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'email', 'contact', 'positionID')
    list_display_links = ('username',)


admin.site.register(Map, MapAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
