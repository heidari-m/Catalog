from django.db import models
from django.urls import reverse

# from .form import *


# Create your models here.


class Contact(models.Model):
    primary_name = models.CharField(max_length=50)
    contact_type = models.ForeignKey('ContactType', on_delete=models.CASCADE)
    primary_note = models.CharField(max_length=200, null=True, blank=True)
    # entity = models.ManyToManyField('Entity')

    def __str__(self):
        return self.primary_name

    def get_absolute_url(self):
        return reverse('contact-detail', args=[str(self.pk)])


class ContactType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('contact-type-detail', args=[str(self.pk)])


class Entity(models.Model):
    name = models.CharField(max_length=50)
    identification_number = models.CharField(max_length=50, blank=True, null=True)
    address_street = models.CharField(max_length=50,blank=True,null=True,help_text="Street")
    street_number = models.CharField(max_length=50,blank=True,null=True,help_text="Street Number")
    phone_number = models.CharField(max_length=15, blank=True,null=True)
    email = models.EmailField(null=True,blank=True)
    note = models.CharField(max_length=200,blank=True,null=True)
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE)
    # contact_person = models.ManyToManyField('Person')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('entity-detail', args=[str(self.pk)])


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    sir_name = models.CharField(max_length=50)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    RELATION_TYPE = (('r','Replacement'),('rp','Report to'),('m','Manager of'),('pe','Peer of'))
    link_to_Other_contact_person = models.CharField(max_length=2,choices=RELATION_TYPE,null=True,blank=True)
    related_person = models.ForeignKey('Person',on_delete=models.SET_NULL,null=True, blank=True)
    note = models.CharField(max_length=200, null=True, blank=True)
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE)
    entity = models.ForeignKey('Entity', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.sir_name}'

    def get_absolute_url(self):
        return reverse('person-detail', args=[str(self.pk)])

