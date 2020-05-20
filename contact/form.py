from django import forms
from django.forms import ModelForm

from .models import Contact, ContactType, Entity, Person
from .widgets import *


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {'contact_type': SelectWithAddContactTypeWidget}

    # def __init__(self,contact, *args, **kwargs):
    #     super(ContactForm, self).__init__(*args, **kwargs)
    #     self.fields['entities'].queryset = Entity.objects.filter(contact=contact)


class ContactTypeForm(ModelForm):
    class Meta:
        model = ContactType
        fields = '__all__'


class EntityForm(ModelForm):
    class Meta:
        model = Entity
        fields = '__all__'


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
