from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(ExtendGroup)
class ExtendGroupAdmin(admin.ModelAdmin):
    pass