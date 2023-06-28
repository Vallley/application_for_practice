from django import template
from ..models import *
from django.db.models import Max

register = template.Library()

def max_num():
    return 8


register.filter('max_num', max_num)