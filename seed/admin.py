from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    pass


@admin.register(SpeciesImage)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(VarietyField)
class VarietyFieldAdmin(admin.ModelAdmin):
    pass


@admin.register(VarietyFieldValue)
class VarietyFieldValueAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Variety)
class VarietyAdmin(admin.ModelAdmin):
    pass


@admin.register(myModel)
class myModelAdmin(admin.ModelAdmin):
    pass


