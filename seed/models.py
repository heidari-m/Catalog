from django.db import models
from django.urls import reverse
import datetime

from . import constant

from os.path import splitext, basename

from .validators import *
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)
from django_currentuser.db.models import CurrentUserField

# Create your models here.


# class Essay(models.Model):
#     essay_min_length = models.IntegerField()
#     essay_max_length = models.IntegerField()
#     help_text = models.CharField()
#     essay_prompt = models.CharField()

class BusinessDivision(models.Model):
    FIELD = (('s','seeds'),('f2','field2'),('f3','field3'))
    business_field = models.CharField(max_length=2, choices=FIELD)

    def __str__(self):
        return f'{self.get_business_field_display()}'

    def get_absolute_url(self):
        return reverse('business-detail', args=[str(self.pk)])


class GlobalCrop(models.Model):
    value = models.CharField(max_length=50)
    business_division = models.ForeignKey('BusinessDivision', on_delete=models.CASCADE)

    def __str__(self):
        return self.value


class CropFamily(models.Model):
    value = models.CharField(max_length=50)
    global_crop = models.ForeignKey('GlobalCrop', on_delete=models.CASCADE)
    business_division = models.ForeignKey('BusinessDivision', on_delete=models.CASCADE)

    def __str__(self):
        return self.value


class Species(models.Model):
    name = models.CharField(max_length=50)
    common_name = models.CharField(max_length=50, null=True, blank=True)
    latin_name = models.CharField(max_length=70, null=True)
    photo = models.ImageField(upload_to='seed/repo/speices/image/', null=True, blank=True)
    #
    # product_life_cycle = models.ForeignKey('ProductLifeCycle', on_delete=models.SET_NULL, null=True)
    crop_family = models.ForeignKey('CropFamily',on_delete=models.CASCADE)
    # business_division = models.ForeignKey('BusinessDivision', on_delete=models.PROTECT)
    #
    seed_count_per_gramme_min_interval = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    seed_count_per_gramme_max_interval = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)

    germination_lasts_year_min_interval = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    germination_lasts_year_max_interval = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)

    SOW_TYPE = (('d', 'DIRECT SOWING'),('t', 'TRANSPLANT'),('b','Both'))
    sow_type = models.CharField(max_length=1, choices=SOW_TYPE, default='b', blank=True, null=True)

    DIRECT_SOWING_TYPE = (('h', 'By Hand'),('m','Machine'))
    direct_sowing_type = models.CharField(max_length=1, choices=DIRECT_SOWING_TYPE, default='h', blank=True, null=True)

    BY_HAND_TYPE = (('s','seed by seed'),('b','broadcasted'))
    hand_type = models.CharField(max_length=1, choices=BY_HAND_TYPE, default='s', blank=True, null=True)

    sow_KG_HA_direct_min_interval = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    sow_KG_HA_direct_max_interval = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)

    sow_KG_HA_transplant_min_interval = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    sow_KG_HA_transplant_max_interval = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)

    depth_type = models.CharField(max_length=1, choices=SOW_TYPE, default='d', blank=True, null=True)
    depth_min_interval = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)
    depth_max_interval = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True)

    distance_CM_row_to_row_min_interval = models.IntegerField(null=True, blank=True)
    distance_CM_row_to_row_max_interval = models.IntegerField(null=True, blank=True)
    distance_CM_plant_to_plant_min_interval = models.IntegerField(null=True, blank=True)
    distance_CM_plant_to_plant_max_interval = models.IntegerField(null=True, blank=True)

    sprouting_time_days_min_interval = models.IntegerField(null=True, blank=True)
    sprouting_time_days_max_interval = models.IntegerField(null=True, blank=True)
    #

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('species-detail', args=[str(self.pk)])


class SpeciesImage(models.Model):
    species = models.ForeignKey('Species', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    photo = models.ImageField(upload_to='seed/gallery', )
    legend = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.legend

    # class Family(models.Model):


class ProductType(models.Model):
    type = models.CharField(max_length=50)
    species = models.ForeignKey('Species',on_delete=models.CASCADE)

    def __str__(self):
        return self.type


#     name = models.CharField(max_length=50)
#     species = models.ForeignKey('Species', on_delete=models.PROTECT)
#     photo = models.ImageField(upload_to='seed/gallery', null=True, blank=True)
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse('familyspecification-detail', args=[str(self.id)])


# class Specification(models.Model):
#     species = models.ForeignKey('Species', on_delete=models.PROTECT)
#     seed_count_per_gramme_min_interval = models.IntegerField(null=True, blank=True)
#     seed_count_per_gramme_max_interval = models.IntegerField(null=True, blank=True)
#     germ_lasts_year_min_interval = models.IntegerField(null=True, blank=True)
#     germ_lasts_year_max_interval = models.IntegerField(null=True, blank=True)
#     SOW_TYPE = (
#         ('d', 'DIRECT SOWING'),
#         ('t', 'TRANSPLANT'),
#         ('m', 'MACHINE SOWING'),
#         ('h', 'BY HAND'),
#     )
#     sow_type1 = models.CharField(max_length=1, choices=SOW_TYPE, default='d', blank=True)
#     sow_KG_HA_min_interval1 = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
#     sow_KG_HA_max_interval1 = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
#     sow_type2 = models.CharField(max_length=1, choices=SOW_TYPE, default='t', blank=True)
#     sow_KG_HA_min_interval2 = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
#     sow_KG_HA_max_interval2 = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
#     DEPTH_TYPE = (
#         ('s', 'SOWING CM'),
#         ('t', 'TRANSPLANT'),
#     )
#     depth_type = models.CharField(max_length=1, choices=DEPTH_TYPE, default='s', blank=True)
#     depth_min_interval = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
#     depth_max_interval = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
#     distance_CM_row_to_row_min_interval = models.IntegerField(null=True, blank=True)
#     distance_CM_row_to_row_max_interval = models.IntegerField(null=True, blank=True)
#     distance_CM_plant_to_plant_min_interval = models.IntegerField(null=True, blank=True)
#     distance_CM_plant_to_plant_max_interval = models.IntegerField(null=True, blank=True)
#     sprouting_time_days_min_interval = models.IntegerField(null=True, blank=True)
#     sprouting_time_days_max_interval = models.IntegerField(null=True, blank=True)
#
#     def __str__(self):
#         return self.species
#
#     # def get_absolute_url(self):
#     #     return reverse('specification-detail', args=[str(self.species_id)])


import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
class Variety(models.Model):
    serial_no = models.CharField(max_length=12, primary_key=True)
    global_crop = models.ForeignKey('GlobalCrop', on_delete=models.CASCADE)
    crop_family = models.ForeignKey('CropFamily', on_delete=models.CASCADE)
    species = models.ForeignKey('Species', on_delete=models.CASCADE)
    product_type = models.ForeignKey('ProductType', on_delete=models.SET_NULL, null=True, blank=True)
    variety_seed_type = models.CharField(max_length=2, choices=constant.SEED_TYPE)
    global_name = models.CharField(max_length=50, blank=True, null=True)
    variety_supplier_name = models.CharField(max_length=50)
    variety_supplier_id = models.CharField(max_length=50, validators=[space_prohibited_validator], null=True, blank=True)
    supplier_contact = models.ForeignKey('contact.Contact', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='seed/repo/variety/image', null=True, blank=True)
    photo_title = models.CharField(max_length=70, null=True, blank=True)
    photo_legend = models.CharField(max_length=100, null=True, blank=True)
    created_by = CurrentUserField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='updated_user')
    group = models.ManyToManyField('auth.Group', null=True, blank=True)

    class Meta:
        permissions = (
            ('group_level', 'Group level'),
        )

    def __str__(self):
        # if self.global_name:
        #     return self.global_name
        return self.variety_supplier_name

    def get_absolute_url(self):
        return reverse('variety-detail', args=[self.serial_no])
        # return reverse('variety-detail', args=[self.serial_no])
        # return reverse('variety-detail', args=[str(self.pk)])

    def shot_image(self, obj):
        return self.photo.url

    def filename(self):
        # return os.path.basename(self.photo.name)
        return basename(splitext(self.photo.name)[0])

    def pdf_url(self):
        return reverse('pdf', args=[str(self.global_name)])

    def save(self, *args, **kwargs):
        if not self.global_name:
            self.global_name = self.variety_supplier_name
        super().save(*args,**kwargs)


class VarietySupplier(models.Model):
    variety = models.OneToOneField('Variety', on_delete=models.CASCADE)
    # name = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to='seed/repo/supplier/image', null=True, blank=True)
    document = models.FileField(upload_to='seed/repo/supplier/document', null=True, blank=True)
    remark = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.variety.variety_supplier_name

    def get_absolute_url(self, *args):
        return reverse('variety-supplier-detail', args=[str(self.id)])


class VarietyBaseData(models.Model):
    variety = models.OneToOneField('Variety', on_delete=models.CASCADE)
    usage = models.CharField(max_length=2, choices=constant.USEAGE, null=True, blank=True)
    ecology = models.CharField(max_length=2, choices=constant.ECOLOGY, null=True, blank=True)
    production_cycle = models.CharField(max_length=2, choices=constant.PRODUCTION_CYCLE, null=True, blank=True)
    color = models.CharField(max_length=2, choices=constant.COLOR, null=True, blank=True)
    technical_description = models.CharField(max_length=300, null=True, blank=True)
    unique_selling_points_and_commercial_positioning = models.CharField(max_length=100, null=True, blank=True)
    competition = models.CharField(max_length=50, null=True, blank=True)
    photo = models.ImageField(upload_to='seed/repo/Bancella/image', null=True, blank=True)
    document = models.FileField(upload_to='seed/repo/Bancella/document', null=True, blank=True)

    def __str__(self):
        return self.usage

    def get_absolute_url(self):
        return reverse('variety-detail', args=[str(self.variety.serial_no)])


class VarietyImage(models.Model):
    variety = models.ForeignKey('Variety', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    photo = models.ImageField(upload_to='seed/repo/variety/image', )
    legend = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.legend


class ProductLifeCycleLog(models.Model):
    variety = models.ForeignKey('Variety', on_delete=models.CASCADE)
    # global_name = models.CharField(max_length=50,)
    # other_global_name = models.CharField(max_length=50, null=True, blank=True)
    global_plc = models.CharField(max_length=2, choices=constant.GLOBAL_PLC)
    global_plc_date = models.DateField(null=True, blank=True)
    global_plc_remark = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['global_plc_date']

    def __str__(self):
        return self.variety.global_name

    def get_absolute_url(self):
        return reverse('product_life_cycle_detail', args=[str(self.pk)])


class CountryPLC(models.Model):
    variety = models.ForeignKey('Variety', on_delete=models.SET_NULL, null=True)
    local_name = models.CharField(max_length=2, choices=constant.GLOBAL_PLC)
    # local_plc_date = models.DateField()
    contact = models.ForeignKey('contact.Contact', on_delete=models.SET_NULL, null=True, blank=True)
    person_in_charge_of_development = models.ForeignKey('contact.Person', on_delete=models.SET_NULL, null=True, blank=True)
    trial_and_development_results = models.CharField(max_length=200, null=True, blank=True)
    go_to_market_approach = models.CharField(max_length=200, null=True, blank=True)
    local_brand = models.CharField(max_length=20, null=True, blank=True)
    local_picture = models.ImageField(upload_to="seed/repo/country_plc/image", null=True, blank=True)
    local_picture = models.FileField(upload_to="seed/repo/country_plc/document", null=True, blank=True)
    remark = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.local_name


class CountryPLCLog(models.Model):
    CountryPLC = models.ForeignKey('CountryPLC', on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=constant.GLOBAL_PLC)
    country_plc_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.status


class Country(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('country-detail', args=[str(self.pk)])


class VarietyField(models.Model):
    field = models.CharField(max_length=50)

    def __str__(self):
        return self.field


class VarietyFieldValue(models.Model):
    variety = models.ForeignKey('Variety', on_delete=models.PROTECT)
    field = models.ForeignKey('VarietyField', on_delete=models.PROTECT)
    value = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.variety} {self.field} {self.value}'


class myModel(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    amount = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)
    model2 = models.ForeignKey('Model2',on_delete=models.SET_NULL,null=True,blank=True)
    ph = models.ImageField(upload_to='', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('myModel-detail', args=[str(self.pk)])


class Model2(models.Model):
    naam = models.CharField(max_length=50)

    def __str__(self):
        return self.naam

