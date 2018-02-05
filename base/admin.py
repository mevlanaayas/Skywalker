from django.contrib import admin

# Register your models here.
from base.models import CustomUser, Map, Label

admin.register(CustomUser)
admin.register(Map)
admin.register(Label)
