from django.shortcuts import render
from seed.models import Species,Family, FamilySpecification, VarietyField, VarietyFieldValue, Variety
from django.views import generic
#
from django_tables2 import SingleTableView, RequestConfig, SingleTableMixin, MultiTableMixin
from .tables import FamilySpecificationTable, VarietyFieldValueTable


# Create your views here.

def index(request):
    context = {'count_species': Species.objects.all().count(),
               'count_varieties': Variety.objects.all().count()}
    return render(request, 'seed/index.html', context=context)


class SpeciesListView(generic.ListView):
    model = Species
    template_name = 'seed/species_list.html'


class SpeciesDetailView(generic.DetailView):
    model = Species

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     species_qs = Species.objects.filter(species=self.kwargs[id]).values()


class FamilyListView(generic.ListView):
    model = Family
    template_name = 'seed/family_list.html'


class FamilyDetailView(generic.DetailView):
    model = Family
    slug_field = 'name'
    slug_url_kwarg = 'str'


class FamilySpecificationDetailView(generic.DetailView):
    model = FamilySpecification
    # slug_field = 'family'
    # slug_url_kwarg = 'str'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     family_specification_qs = FamilySpecification.objects.filter(family__familyspecification=kwargs['object'].id)
    #     context['family_specification_value'] = family_specification_qs.values()
    #     context['table'] = FamilySpecificationTable(family_specification_qs)
    #     return context


class VarietyDetailView(generic.DetailView):
    model = Variety
    # slug_field = 'name'
    # slug_url_kwarg = 'str'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        variety_qs = VarietyFieldValue.objects.filter(variety_id__exact=kwargs['object'].id)
        context['table'] = VarietyFieldValueTable(variety_qs)
        return context