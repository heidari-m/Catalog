from django.core.validators import ValidationError
from django.utils.translation import gettext_lazy as _


def space_prohibited_validator(value):
    if ' ' in value:
        raise ValidationError(_('%(value)s contains space'),params={'value':value})


# def uniqe_validator(value):
#     from seed.models import Variety
#     qs = Variety.objects.filter(variety_supplier_name=value)
#     if qs.exists():
#         raise ValidationError(_('%(value)s already exists'),params={'value':value})
    