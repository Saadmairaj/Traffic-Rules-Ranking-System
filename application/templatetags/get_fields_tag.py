from django import template

register = template.Library()


@register.filter
def get_fields(obj):
    for field in obj._meta.get_fields():
        yield field
