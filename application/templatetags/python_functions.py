from django import template

register = template.Library()


@register.filter
def endswith(data: str, check_with: str):
    return str(data).endswith(check_with)