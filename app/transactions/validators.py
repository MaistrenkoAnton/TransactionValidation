import pycountry
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers


def is_valid_currency(value):
    if not [currency.alpha_3 for currency in pycountry.currencies if currency.alpha_3 == value]:
        raise serializers.ValidationError(_('Currency name is not valid.'))
