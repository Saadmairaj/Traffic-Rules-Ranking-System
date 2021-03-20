from django import template
from django.contrib.auth.models import User
from application import models

register = template.Library()


@register.filter
def get_user_model(obj=None):
    if obj:
        return User.objects.values_list(obj, flat=True)
    return User.objects.filter()


@register.filter
def get_police_model(obj=None):
    if obj:
        return models.PoliceStation.objects.values_list(obj, flat=True)
    return models.PoliceStation.objects.filter()


@register.filter
def get_complaint_status(ag=None):
    return [i[0] for i in models.Complaint.STATUS]


@register.filter
def get_complaint_type(ag=None):
    return [i[0] for i in models.Complaint.TYPE]
