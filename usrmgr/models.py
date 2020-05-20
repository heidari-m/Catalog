from django.db import models
from django.urls import reverse
import datetime

from os.path import splitext, basename

from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)
from django_currentuser.db.models import CurrentUserField




# Create your models here.
class ExtendGroup(models.Model):
    group = models.OneToOneField('auth.Group', on_delete=models.SET_NULL, null=True)
    country = models.ManyToManyField('seed.Country', null=True)


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
