from django.contrib import admin
from .models import Species,Family,FamilySpecification,VarietyField,VarietyFieldValue,Variety

# Register your models here.

@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    pass


@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    pass


@admin.register(FamilySpecification)
class FamilySpecificationAdmin(admin.ModelAdmin):
    pass


@admin.register(VarietyField)
class VarietyFieldAdmin(admin.ModelAdmin):
    pass


@admin.register(VarietyFieldValue)
class VarietyFieldValueAdmin(admin.ModelAdmin):
    pass


@admin.register(Variety)
class VarietyAdmin(admin.ModelAdmin):
    pass
