from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from seed.models import *
from django.views import generic
#
from django_tables2 import SingleTableView, RequestConfig, SingleTableMixin, MultiTableMixin
from .tables import *
#
from seed.utils import render_to_pdf
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
#
from django.core import serializers
#
# from django.views.generic import View
import datetime
#
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
#
from .forms import *
import json

#
from dal import autocomplete


class AutoView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return ProductType.objects.none()
        qs = ProductType.objects.all()
        if self.q:
            qs = qs.filter(type__icontains=self.q)
        return qs


def all_link(request):
    return render(request, 'seed/all_link.html')


# Create your views here.

def index(request):
    context = {'count_species': Species.objects.all().count(),
               'count_varieties': Variety.objects.all().count()}
    return render(request, 'seed/index.html', context=context)


class BusinessDivisionListView(generic.ListView):
    model = BusinessDivision
    template_name = 'seed/business_division_list.html'


class BusinessDivisionCreate(generic.CreateView):
    model = BusinessDivision
    template_name = 'seed/business_division_form.html'
    fields = '__all__'


def business_division_create(request):
    if request.method == "POST":
        form = BusinessDivisionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BusinessDivisionForm()
        return render(request, 'seed/business_division_form.html', {'form': form})


def global_crop_create(request):
    if request.method == 'POST':
        form = GlobalCropForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = GlobalCropForm()
        return render(request, 'seed/global_crop_form.html', {'form': form})


def crop_family_create(request):
    if request.method == 'POST':
        form = CropFamilyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CropFamilyForm()
        return render(request, 'seed/crop_family_form.html', {'form': form})


class SpeciesListView(generic.ListView):
    model = Species
    template_name = 'seed/species_list.html'


class SpeciesCreate(generic.CreateView):
    model = Species
    # template_name = 'seed/species_form.html'
    # fields = '__all__'
    form_class = SpeciesForm
    success_url = reverse_lazy('species')


class SpeciesUpdate(generic.UpdateView):
    model = Species
    fields = '__all__'


class SpeciesDelete(generic.DeleteView):
    model = Species
    fields = '__all__'


class SpeciesDetailView(generic.DetailView):
    model = Species

    # slug_field = 'species'
    # slug_url_kwarg = 'str'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = SpeciesImage.objects.filter(species_id=kwargs['object'].pk)
        return context


class SpeciesImageListView(generic.ListView):
    model = SpeciesImage
    template_name = 'seed/image_list.html'


def product_type_create(request):
    if request.method == "POST":
        form = ProductTypeForm(request.POST)
        if form.is_valid():
            # form.save()
            instance = form.save()
            # product_type_list = ProductType.objects.all()
            # return render(request, 'seed/product_type_dropdown_list_options.html',
            #               {'product_type_list': product_type_list})
            return HttpResponse(
                '<script>opener.closePopup(window, "%s", "%s", "#id_product_type");</script>' % (instance.pk, instance.type))
        return render(request, 'seed/product_type_form.html', {'form': form})
    else:
        form = ProductTypeForm()
        return render(request, 'seed/product_type_form.html', {'form': form})


# class ImageCreate(generic.CreateView):
#     model = SpeciesImage
#     template_name = 'seed/image_form.html'
#     fields = '__all__'


def image_create(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            m = form.save()
            m.save()
            return redirect('/')
    else:

        form = ImageForm()
        return render(request, 'seed/image_form.html', {'form': form})


# class SpecificationDetailView(generic.DetailView):
#     model = Specification
#     # slug_field = 'species'
#     # slug_url_kwarg = 'str'
#
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     family_specification_qs = FamilySpecification.objects.filter(family__familyspecification=kwargs['object'].id)
#     #     context['family_specification_value'] = family_specification_qs.values()
#     #     context['table'] = FamilySpecificationTable(family_specification_qs)
#     #     return context
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['variety_list'] = Variety.objects.filter(species_id=self.kwargs['pk'])
#         return context


class VarietyList(generic.ListView):
    model = Variety


class VarietyDetailView(generic.DetailView):
    model = Variety
    slug_field = 'serial_no'
    slug_url_kwarg = 'str'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['variety_serial'] = self.kwargs['str']
        return context
    #     variety_qs = VarietyFieldValue.objects.filter(variety_id__exact=kwargs['object'].id)
    #     # temp part
    #     # context = {'table': VarietyFieldValueTable(variety_qs),
    #     #            }
    #     # end temp
    #
    #     context['table'] = VarietyFieldValueTable(variety_qs)
    #     return context
    # def generate_pdf(self, **kwargs):
    #     variety_qs = VarietyFieldValue.objects.filter(variety_id__exact=kwargs['object'].id)
    #     context = {'table': VarietyFieldValueTable(variety_qs),
    #                'variety': variety_qs}
    #     # data = {
    #     #     'today': datetime.date.today(),
    #     #     'amount': 'tesssssst',
    #     #     'customer_name': 'Cooper Mann',
    #     #     'order_id': 1233434,
    #     # }
    #     # pdf = render_to_pdf('seed/invoice.html', data)
    #     pdf = render_to_pdf('seed/invoice.html', context)
    #     return HttpResponse(pdf, content_type='application/pdf')


from django.shortcuts import render_to_response


def variety_create(request):
    # request should be ajax and method should be POST.
    # if request.is_ajax and request.method == "POST":
    if (request.method == "POST"):
        form = VarietyForm(request.POST, request.FILES)
        # save the data and after fetch the object in instance
        if form.is_valid():
            form.save()
            # instance = form.save()
            # serialize in new object in json
            # ser_instance = serializers.serialize('json', [instance, ])
            # send to client side.
            # return JsonResponse({"instance": ser_instance}, status=200)
            return redirect('varieties')
        return render(request, 'seed/variety_form.html', {'form': form})
    else:
        form = VarietyForm()
        return render(request, 'seed/variety_form.html', {'form': form})


def load_crop_family(request):
    global_crop_id = request.GET.get('global_crop_id')
    if global_crop_id:
        crop_family = CropFamily.objects.filter(global_crop=global_crop_id)
    else:
        crop_family = CropFamily.objects.all()
    return render(request, 'seed/crop_family_dropdown_list_options.html', {'crop_family': crop_family})


def load_species(request):
    crop_family_id = request.GET.get('crop_family_id')
    if crop_family_id:
        species = Species.objects.filter(crop_family=crop_family_id)
    else:
        species = Species.objects.all()
    return render(request, 'seed/species_dropdown_list_options.html', {'species': species})


def load_product_type(request):
    product_type_list = ProductType.objects.all()
    return render(request, 'seed/product_type_dropdown_list_options.html', {'product_type_list': product_type_list})


# def variety_update(request, str):
#     if (request.method == 'POST'):
#         form = VarietyForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('variety-detail', str)
#         return render(request, 'seed/variety_form.html', {'form':form})
#     form = VarietyForm()
#     return render(request, 'seed/variety_form.html', {'form':form})


class VarietyUpdate(generic.UpdateView):
    model = Variety
    # fields = '__all__'
    form_class = VarietyForm
    slug_field = 'serial_no'
    slug_url_kwarg = 'str'


from http import HTTPStatus


def validate_variety_supplier_name(request):
    variety_name = request.GET.get('variety_supplier_name', None)
    qs = Variety.objects.filter(variety_supplier_name__icontains=variety_name)
    data = {
        'similar_exists': qs.exists()
    }
    if data['similar_exists']:
        data['similar'] = qs[0].variety_supplier_name
        data['contact'] = qs[0].supplier_contact.primary_name
        data['error_message'] = 'Similar variety "%s" from "%s" exists.' % (data['similar'], data['contact'])
        # data['status'] = 'false'
        res = JsonResponse(data)
        # res.status_code = 500
        return res
    return JsonResponse(data)


def variety_image_create(request):
    if request.method == "POST":
        form = VarietyImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = VarietyImageForm()
        return render(request, 'seed/general_image_form.html', {'form': form})


def tmp(request):
    var_tmp = request.GET.get('tmp_var', None)
    sup = VarietySupplier.objects.filter(id=var_tmp)
    form = VarietySupplierForm()
    if request.is_ajax:
        form = VarietySupplierForm()
    # if request.is_ajax and request.method == "POST":
    #     form = (request.POST)
    #     # save the data and after fetch the object in instance
    #     if form.is_valid():
    #         instance  = form.save()
    #         # serialize in new object in json
    #         ser_instance = serializers.serialize('json',[instance,])
    #         # send to client side.
    #         return JsonResponse({"instance": ser_instance}, status=200)
    #         # return redirect('/')
    #     else:
    #         # form = VarietyForm()
    #         # return render(request, 'seed/variety_form.html', {'form':form})
    #         # some form errors occured.
    #         return JsonResponse({"error": form.errors}, status=400)
    # # some error occured
    # form = VarietyForm()
    # data = {
    #     'myform': form,
    # }
    # return JsonResponse(data)
    return render(request, 'seed/tmp_form.html', {'form': form})


class VarietySupplierList(generic.ListView):
    model = VarietySupplier
    template_name = 'seed/variety_supplier_list.html'


class VarietySupplierDetail(generic.DetailView):
    model = VarietySupplier
    template_name = 'seed/variety_supplier_detail.html'
    # slug_field = 'id'
    # slug_url_kwarg = 'str'


class VarietySupplierUpdate(generic.UpdateView):
    model = VarietySupplier
    template_name = 'seed/variety_supplier_form.html'
    fields = '__all__'
    # slug_field = 'id'
    # slug_url_kwarg = 'str'


def variety_supplier_detail2(request):
    var_tmp = request.GET.get('tmp_var', None)
    sup = VarietySupplier.objects.get(variety=var_tmp)
    return render(request, 'seed/variety_supplier_detail2.html', {'varietysupplier': sup})


def variety_supplier_create(request, str):
    if request.is_ajax and request.method == "POST":
        form = VarietySupplierForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new object in json
            ser_instance = serializers.serialize('json', [instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
            return redirect('/')
        else:
            # form = VarietyForm()
            # return render(request, 'seed/variety_form.html', {'form':form})
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)
    # some error occured
    form = VarietySupplierForm(initial={'variety': str})
    return render(request, 'seed/variety_supplier_form.html', {'form': form})


class AjaxableResponseMixin:
    """
        Mixin to add AJAX support to a form.
        Must be used with an object-based FormView (e.g. CreateView)
        """

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class VarietyBaseDataUpdate(AjaxableResponseMixin, generic.UpdateView):
    model = VarietyBaseData
    fields = '__all__'
    template_name = 'seed/variety_base_data_form.html'


def variety_basedata_update(request):
    id = request.GET.get('variety_id', None)
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(VarietyBaseData, id=id)

    # pass the object as instance in form
    form = VarietyBaseDataForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

        # add form dictionary to context
    context["form"] = form

    return render(request, "seed/variety_base_data_form.html", context)


class VarietyBaseDataDetail(generic.DetailView):
    model = VarietyBaseData
    template_name = 'seed/variety_base_data_detail.html'


def variety_base_data_detail(request):
    # pass data to variety-detail view
    variety_id = request.GET.get('variety_id', None)
    variety_base_data = VarietyBaseData.objects.get(variety=variety_id)
    return render(request, 'seed/variety_base_data_detail.html', {'varietybasedata': variety_base_data})


def variety_base_data_update(request):
    variety_base_data_id = request.GET.get('variety_base_data_id', None)
    variety_base_data = VarietyBaseData.objects.get(id=variety_base_data_id)
    return render(request, 'seed/variety_base_data_form.html', {'varietybasedata': variety_base_data})


def variety_base_data_create(request, str):
    if request.is_ajax and request.method == "POST":
        form = VarietyBaseDataForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new object in json
            ser_instance = serializers.serialize('json', [instance, ])
            # send to client side.
            # return JsonResponse({"instance": ser_instance}, status=200)
            return redirect('variety-detail', str)
        else:
            return JsonResponse({"error": form.errors}, status=400)
    # some error occured
    form = VarietyBaseDataForm(initial={'variety': str})
    return render(request, 'seed/variety_base_data_form.html', {'form': form})


def load_contact_entity(request):
    contact = request.GET.get('contact')
    entities = Entity.objects.filter(contact=contact).order_by('name')
    return render(request, 'seed/entities_dropdown_list_options.html', {'entities': entities})


def load_contact_person(request):
    contact = request.GET.get('contact')
    persons = Person.objects.filter(contact=contact)
    return render(request, 'seed/persons_dropdown_list_options.html', {'persons': persons})


class ProductLifeCycleList(generic.ListView):
    model = ProductLifeCycle
    template_name = 'seed/product_life_cycle_list.html'


class ProductLifeCycleDetail(generic.DetailView):
    model = ProductLifeCycle
    template_name = 'seed/product_life_cycle_detail.html'


def product_life_cycle_create(request):
    if request.is_ajax and request.method == "POST":
        form = ProductLifeCycleForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new object in json
            ser_instance = serializers.serialize('json', [instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
            return redirect('/')
        else:
            # form = VarietyForm()
            # return render(request, 'seed/variety_form.html', {'form':form})
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)
    # some error occured
    form = ProductLifeCycleForm()
    return render(request, 'seed/product_life_cycle_form.html', {'form': form})


class ProductLifeCycleUpdate(generic.UpdateView):
    model = ProductLifeCycle
    template_name = 'seed/product_life_cycle_form.html'
    # fields = '__all__'
    form_class = ProductLifeCycleForm


def plc_manage_add(request, str):
    # a = request.session['variety_serial']
    qs = ProductLifeCycle.objects.filter(variety=str)
    table = PLCTable(qs)
    if request.method == 'POST':
        form = PLCManageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('variety-detail', str)
        return render(request, 'seed/plc_manage_add.html', {'form': form, 'table': table})
    else:
        form = PLCManageForm(initial={'variety': str})
        # form = PLCManageForm(initial={'variety':request.session['variety_serial']})
        return render(request, 'seed/plc_manage_add.html', {'form': form, 'table': table})


def country_plc_create(request):
    if request.is_ajax and request.method == "POST":
        form = CountryPLCForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new object in json
            ser_instance = serializers.serialize('json', [instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
            return redirect('/')
        else:
            # form = VarietyForm()
            # return render(request, 'seed/variety_form.html', {'form':form})
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)
    # some error occured
    form = CountryPLCForm()
    return render(request, 'seed/country_plc_form.html', {'form': form})


def variety_serial_no(request):
    # species_id = request.GET.get('species_id', None)
    crop_family = request.GET.get('crop_family', None)
    crop_family_qs = CropFamily.objects.get(id=crop_family)
    # business_division_qs = BusinessDivision.objects.get(id=species_id).business_field
    if crop_family_qs:
        # qs = qs.values()[0]
        variety_serial = (crop_family_qs.business_division.business_field + crop_family_qs.value[0:2]).upper()
        qs2 = Variety.objects.filter(serial_no__startswith=variety_serial).order_by('serial_no').last()
        if not qs2:
            qs2 = Variety()
            qs2.serial_no = variety_serial + '0AA00'
        counter = qs2.serial_no[3:8]
        int_1digit_counter = int(counter[0])
        int_2last_counter = int(counter[3:5])
        if int_2last_counter + 1 > 99:
            int_2last_counter = 0
            if ord(counter[2]) >= 90:
                if ord(counter[1]) >= 90:
                    int_1digit_counter += 1
                    new_serial = qs2.serial_no[0:3] + str(int_1digit_counter) + 'AA' + "0" + str(
                        int_2last_counter) + qs2.serial_no[8:12]
                else:
                    new_serial = qs2.serial_no[0:3] + counter[0] + chr(ord(counter[1]) + 1) + 'A' + "0" + str(
                        int_2last_counter) + qs2.serial_no[8:12]
            else:
                new_serial = qs2.serial_no[0:3] + counter[0:2] + chr(ord(counter[2]) + 1) + "0" + str(
                    int_2last_counter) + qs2.serial_no[8:12]
        else:
            if int_2last_counter + 1 > 9:
                new_serial = qs2.serial_no[0:3] + counter[0:3] + str(int_2last_counter + 1) + qs2.serial_no[8:12]
            else:
                new_serial = qs2.serial_no[0:3] + counter[0:3] + "0" + str(int_2last_counter + 1) + qs2.serial_no[8:12]

        # variety_serial +=
    else:
        new_serial = "Business field is not defined"
    data = {
        'serial_no': new_serial,
    }
    return JsonResponse(data)


def variety_field_create(request):
    if request.method == "POST":
        form = VarietyFieldForm(request.POST)
        if form.is_valid():
            m = form.save()
            m.save()
            return redirect('/')
    else:
        form = VarietyFieldForm()
        return render(request, 'seed/variety_field_form.html', {'form': form})


def variety_field_value_create(request):
    if request.method == "POST":
        form = VarietyFieldValueForm(request.POST)
        if form.is_valid():
            m = form.save()
            m.save()
            return redirect('/')
    else:
        form = VarietyFieldValueForm()
        return render(request, 'seed/variety_field_value_form.html', {'form': form})


from django.template.loader import get_template

from .render import Render


class GeneratePdf2(generic.DetailView):

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # variety_qs = VarietyFieldValue.objects.filter(variety_id__exact=kwargs['pk'])
    #     variety_qs = VarietyFieldValue.objects.filter(variety_id__exact=kwargs['object'].id)
    #     # context['table'] = VarietyFieldValueTable(variety_qs)
    #     context['today'] = datetime.date.today()
    #     # context = {'table': VarietyFieldValueTable(variety_qs.values()),
    #     #            'vars': variety_qs,
    #     #            'today': datetime.date.today(),
    #     #            }
    #     data = {
    #         'today': datetime.date.today(),
    #         'amount': 39.99,
    #         'customer_name': 'Cooper Mann',
    #         'order_id': 1233434,
    #         'vars': vars,
    #     }
    #     return Render.render('seed/invoice.html', data)

    def get(self, request, **kwargs):
        vars = Variety.objects.all()
        variety = Variety.objects.get(id=kwargs['pk'])
        data = {
            'today': datetime.date.today(),
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
            'variety': variety,
            'vars': vars,
            'request': request
        }
        return Render.render('seed/invoice.html', data)


class GeneratePdf(generic.View):

    def get(self, request, *args, **kwargs):
        data = {
            'today': datetime.date.today(),
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('seed/invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class myModelListView(generic.ListView):
    model = myModel


from .forms import myModelForm, Model2Form


def add_myModel(request):
    if request.method == "POST":
        form = myModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = myModelForm()
        return render(request, 'seed/mymodel_form.html', {'form': form})


def add_model2_createpopup(request):
    form = Model2Form(request.POST or None)
    if form.is_valid():
        instancee = form.save()
        return HttpResponse(
            '<script>opener.closePopup(window, "%s", "%s", "#id_model2");</script>' % (instancee.pk, instancee))
    return render(request, "seed/model2_form.html", {"form": form})


def model2_edit_popup(request, pk=None):
    instance = get_object_or_404(Model2, pk=pk)
    form = Model2Form(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save()
        ## Change the value of the "#id_author". This is the element id in the form
        return HttpResponse(
            '<script>opener.closePopup(window, "%s", "%s", "#id_model2");</script>' % (instance.pk, instance))
    return render(request, "seed/model2_form.html", {"form": form})


def get_model2_id(request):
    if request.is_ajax():
        model2_naam = request.GET['model2_naam']
        model2_id = Model2.objects.get(naam=model2_naam).id
        data = {'model2_id': model2_id, }
        return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponse("/")


class myModelDeatilView(generic.DetailView):
    model = myModel


from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
# def generate_pdf(request):
#     species = Species.objects.all()
#     html_string = render_to_string('seed/species_detail.html',{'species':species})
#     html = HTML(string=html_string)
#     result = html.write_pdf()
#
#     response = HttpResponse(content_type='application/pdf;')
#     response['Content-Disposition'] = 'inline; filename=list_people.pdf'
#     response['Content-Transfer-Encoding'] = 'binary'
#
#     with tempfile.NamedTemporaryFile(delete=True) as output:
#         output.write(result)
#         output.flush()
#         output = open(output.name, 'r')
#         # output = output.seek(0)
#         response.write(output.read())
#     return response

from django.template import loader, RequestContext


def generate_pdf(request):
    species = Species.objects.get(id=3)
    template = loader.get_template('seed/species_detail.html')
    html = template.render({'species': species})
    response = HttpResponse(content_type='application/pdf')
    HTML(string=html).write_pdf(response)
    return response


from seed.forms import NameForm, ContactForm


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'seed/name.html', {'form': form})


from django.core.mail import send_mail


def handle_this(request):
    form = ContactForm()
    return render(request, 'seed/contact.html', {'form': form})
