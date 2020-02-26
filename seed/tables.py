import django_tables2 as tables
from django_tables2.utils import A
from .models import Species, Family, FamilySpecification, VarietyFieldValue, VarietyField, Variety
from django.contrib.auth.mixins import LoginRequiredMixin


class VarietyFieldValueTable(tables.Table):

    class Meta:
        model = VarietyFieldValue
        template_name = 'django_tables2/bootstrap4.html'
        fields = ('field','value')


class FamilySpecificationTable(tables.Table):

    class Meta:
        model = FamilySpecification
        template_name = 'django_tables2/bootstrap4.html'