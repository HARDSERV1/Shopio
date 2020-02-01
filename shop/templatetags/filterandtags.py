from django import template

register = template.Library()
from  ..models import Photos


@register.simple_tag()
def get_l(g):
    return Photos.objects.filter(location=g)

@register.simple_tag()
def get_n(g,b,c):
    smth = None
    for i in Photos.objects.filter(location=g):
        if i!=b and i!=c:
            smth = i

    return smth


