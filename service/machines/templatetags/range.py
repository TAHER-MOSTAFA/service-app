from django import template

register = template.Library()

@register.filter(name='range')
def get_range(value):
    return range(int(value))

@register.filter(name='restFive')
def rest_of_stars(value):
    return range(int(5 - value))