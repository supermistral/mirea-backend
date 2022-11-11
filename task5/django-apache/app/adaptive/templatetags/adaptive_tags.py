from django import template
from django.conf import settings


register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, None)
