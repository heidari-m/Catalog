from django.core.validators import ValidationError
from django.utils.translation import gettext_lazy as _


def space_prohibited_validator(value):
    if ' ' in value:
        raise ValidationError(_('%(value)s contains space'),params={'value':value})
    