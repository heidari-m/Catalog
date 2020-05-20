from django.forms import widgets
from django.contrib.admin.widgets import *


class SelectWithAddContactTypeWidget(forms.Select):
    template_name = 'contact/selectwithadd_contact_type.html'