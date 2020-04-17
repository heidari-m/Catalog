from django.shortcuts import render
from django.views import generic
from .models import *
from .form import *
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.


class ContactList(generic.ListView):
    model = Contact
    template_name = 'contact/general_list.html'


class ContactDetail(generic.DetailView):
    model = Contact
    template_name = "contact/contact_detail.html"


def contact_create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            m = form.save()
            m.save()
            return redirect('/')
    else:
        form = ContactForm()
        return render(request, 'contact/contact_form.html', {'form':form})


class ContactTypeList(generic.ListView):
    model = ContactType
    template_name = "contact/general_list.html"


class ContactTypeDetail(generic.DetailView):
    model = ContactType
    template_name = "contact/contact_type_detail.html"


def contact_type_create(request):
    if request.method == "POST":
        form = ContactTypeForm(request.POST)
        if form.is_valid():
            m = form.save()
            m.save()
            return redirect('/')
    else:
        form = ContactTypeForm()
        return render(request, 'contact/contact_form.html', {'form':form})


class EntityList(generic.ListView):
    model = Entity
    template_name = "contact/general_list.html"


class EntityDetail(generic.DetailView):
    model = Entity
    template_name = "contact/entity_detail.html"


def entity_create(request):
    if request.method == "POST":
        form = EntityForm(request.POST)
        if form.is_valid():
            m = form.save()
            m.save()
            return redirect('/')
    else:
        form = EntityForm()
        return render(request, 'contact/contact_form.html', {'form':form})


class PersonList(generic.ListView):
    model = Person
    template_name = "contact/general_list.html"


class PersonDetail(generic.DetailView):
    model = Person
    template_name = "contact/person_detail.html"


def person_create(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            m = form.save()
            m.save()
            return redirect('/')
    else:
        form = PersonForm()
        return render(request, 'contact/contact_form.html', {'form':form})
