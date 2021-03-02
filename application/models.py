import os
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils import timezone
from django.core.mail import EmailMessage, send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.deconstruct import deconstructible


@deconstructible
class ContentFileName:
    def __init__(self, prefix):
        self.prefix = prefix
    
    def __call__(self, instance, org_filename):
        ext = org_filename.split('.')[-1]
        if isinstance(instance, Profile):
            filename = "%s_%s.%s" % (
                self.prefix, instance.user, 'pdf')
        elif isinstance(instance, Vehicle):
            filename = "%s_%s.%s" % (
                self.prefix, instance.vehicle_no, ext)
        path = os.path.join('uploads', filename)
        if os.path.exists(os.path.realpath(path)):
            os.remove(path)
        return path


class PoliceStation(models.Model):
    station_incharge = models.OneToOneField(
        User, on_delete=True, verbose_name='Station In Charge')
    station_city = models.CharField(
        max_length=100, unique=True, verbose_name='Police Status')
    address = models.TextField(max_length=200)
    no_of_employee = models.IntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.station_city)


class Profile(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    police_station = models.ForeignKey(
        PoliceStation, on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(
        max_length=20, choices=GENDER_CHOICES, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    pin = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    drivers_licence_no = models.CharField(
        max_length=100, blank=True, null=True)
    licence_valid_date = models.DateField(
        max_length=100, blank=True, null=True)
    licence_issue_state = models.CharField(
        max_length=100, blank=True, null=True)
    licence_img = models.FileField(upload_to=ContentFileName(
        'licence'), verbose_name=("Driver Licence (Images/PDF)"), null=True, blank=True)
    
    class Meta:
        ordering = ('-user__date_joined', )
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Contact(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=255, null=False, blank=False)
    mobile = models.CharField(max_length=20, null=False, blank=False)
    message = models.CharField(max_length=500, null=False, blank=False)
    status = models.PositiveSmallIntegerField(db_index=False, default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)


class Complaint(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Resolved', 'Resolved'),
        ('Reject', 'Reject'),
        ('Paid', 'Paid'),
        ('Due', 'Due'),
    )
    TYPE = (
        ('FIR', 'FIR'),
        ('Challan', 'Challan'),
        ('Other', 'Other')
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    complaint_type = models.CharField(max_length=50, choices=TYPE)
    police_station = models.ForeignKey(
        PoliceStation, on_delete=models.CASCADE, verbose_name='Police Sttion')
    complaint = models.TextField(max_length=500)
    challan_amount = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS, default="Pending")
    resolved_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="pemployee")
    resolved_date = models.DateTimeField(null=True, blank=True)
    resolved_message = models.CharField(max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.complaint_type)
    

    def save(self, *args, **kwargs):
        subject = f"{self.complaint_type} complaint from Traffic Police"
        message = f"Hi {self.user.first_name}, \n"\
                  f"A {self.complaint_type} complaint of {self.complaint} "\
                  f"has been reported against {self.user.first_name} {self.user.last_name}"\
                  f" on {self.date_created} of {self.challan_amount} fee." \
                  f"\n\n"\
                  f"Thanking You\n"\
                  f"Traffic Police"
        
        if self.complaint_type == 'FIR':
            message = message.replace('against', 'for').replace(' of 0 fee', '')
        
        elif self.complaint_type == 'Other':
            subject = "Complaint from Traffic Police"

        send_mail(
            subject=subject, 
            message=message, 
            from_email='testpython06@gmail.com',
            recipient_list=[self.user.email, ],
            fail_silently=False)
        return super().save(*args, **kwargs)


class Company(models.Model):
    compnay_name = models.CharField(max_length=100)
    company_website = models.CharField(max_length=200, null=True, blank=True)
    company_address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.compnay_name)


class Vehicle(models.Model):
    FUEL = (
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('CNG/LPG', 'CNG/LPG'),
        ('Petrol + CNG', 'Petrol + CNG')
    )

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)    
    vehicle_no = models.CharField(max_length=20, unique=True)
    model_no = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=20, choices=FUEL)
    manufacute_year = models.CharField(max_length=100, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    registered_address = models.CharField(
        max_length=200, null=True, blank=True)
    registered_district = models.CharField(
        max_length=100, null=True, blank=True)
    registered_state = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    rc_img = models.FileField(upload_to=ContentFileName(
        'rc'), verbose_name=("RC (Images/PDF)"), null=True, 
        blank=True)
    insurance_no = models.CharField(
        max_length=30, unique=True, null=True, blank=True)
    insurance_img = models.FileField(upload_to=ContentFileName(
        'insurance'), verbose_name=("Insurance (Images/PDF)"), 
        null=True, blank=True)
    insurance_date = models.DateField(verbose_name=(
        "Insurance Validity"), null=True, blank=True)
    pollution_img = models.FileField(upload_to=ContentFileName(
        'pollution'), verbose_name=("Pollution (Images/PDF)"), 
        null=True, blank=True)
    pollution_date = models.DateField(verbose_name=(
        "Pollution Validity"), null=True, blank=True)

    def __str__(self):
        return "{}".format(self.vehicle_no)


class Upload(models.Model):

    pass
