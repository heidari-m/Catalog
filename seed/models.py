from django.db import models
from django.urls import reverse


# Create your models here.


class Species(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50, null=True)
    photo = models.ImageField(upload_to='seed/gallery', null=True, blank=True)
    # code = models.CharField(max_length=10, null=True, blank=True)
    # crop = models.ForeignKey('Crop', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('species-detail', args=[str(self.id)])


class Family(models.Model):
    name = models.CharField(max_length=50)
    species = models.ForeignKey('Species', on_delete=models.PROTECT)
    photo = models.ImageField(upload_to='seed/gallery', null=True, blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('familyspecification-detail', args=[str(self.id)])


class FamilySpecification(models.Model):
    family = models.ForeignKey('Family', on_delete=models.PROTECT)
    seed_count_per_gramme_min_interval = models.IntegerField(null=True, blank=True)
    seed_count_per_gramme_max_interval = models.IntegerField(null=True, blank=True)
    germ_lasts_year_min_interval = models.IntegerField(null=True, blank=True)
    germ_lasts_year_max_interval = models.IntegerField(null=True, blank=True)
    SOW_TYPE = (
        ('d', 'DIRECT SOWING'),
        ('t', 'TRANSPLANT'),
        ('m', 'MACHINE SOWING'),
        ('h', 'BY HAND'),
    )
    sow_type1 = models.CharField(max_length=1, choices=SOW_TYPE, default='d', blank=True)
    sow_KG_HA_min_interval1 = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sow_KG_HA_max_interval1 = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sow_type2 = models.CharField(max_length=1, choices=SOW_TYPE, default='t', blank=True)
    sow_KG_HA_min_interval2 = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sow_KG_HA_max_interval2 = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    DEPTH_TYPE = (
        ('s', 'SOWING CM'),
        ('t', 'TRANSPLANT'),
    )
    depth_type = models.CharField(max_length=1, choices=DEPTH_TYPE, default='s', blank=True)
    depth_min_interval = models.IntegerField(null=True, blank=True)
    depth_max_interval = models.IntegerField(null=True, blank=True)
    distance_CM_row_to_row_min_interval = models.IntegerField(null=True, blank=True)
    distance_CM_row_to_row_max_interval = models.IntegerField(null=True, blank=True)
    distance_CM_plant_to_plant_min_interval = models.IntegerField(null=True, blank=True)
    distance_CM_plant_to_plant_max_interval = models.IntegerField(null=True, blank=True)
    sprouting_time_days_min_interval = models.IntegerField(null=True, blank=True)
    sprouting_time_days_max_interval = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.family.name

    def get_absolute_url(self):
        return reverse('familyspecification-detail', args=[str(self.id)])


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


class Variety(models.Model):
    name = models.CharField(max_length=50)
    species = models.ForeignKey('Species', on_delete=models.PROTECT)
    family = models.ForeignKey('Family', on_delete=models.PROTECT)
    photo = models.ImageField(upload_to='seed/gallery', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('variety-detail', args=[str(self.name)])

    def shot_image(self, obj):
        return self.photo.url
