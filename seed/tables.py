import django_tables2 as tables
from django_tables2.utils import A
# from .models import Species, VarietyFieldValue, VarietyField, Variety
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin


class PLCTable(tables.Table):
    class Meta:
        model = ProductLifeCycleLog
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['global_plc','global_plc_date']




class VarietyFieldValueTable(tables.Table):

    class Meta:
        model = VarietyFieldValue
        template_name = 'django_tables2/bootstrap4.html'
        fields = ('field','value')


class FamilySpecificationTable(tables.Table):

    class Meta:
        model = Species
        template_name = 'django_tables2/bootstrap4.html'


class SearchResultTable(tables.Table):
    chh = tables.CheckBoxColumn()
    class Meta:
        model = Variety
        'django_tables2/bootstrap4.html'
        fields = ('serial_no','species','variety_supplier_name')