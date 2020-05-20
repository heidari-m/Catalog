from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from seed.models import *
from django.views import generic
#
from django_tables2 import SingleTableView, RequestConfig, SingleTableMixin, MultiTableMixin
#
from seed.utils import render_to_pdf
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseForbidden
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

# Create your views here.
