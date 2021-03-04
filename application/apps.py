import datetime
from event import timethread, run_once
from django.apps import AppConfig
from django.core.mail import send_mail
from functools import partial


def email_details(name, doc, vehicle_no, over_due=False):
    message = f"Hi {name}!\n"\
              f"This is to remind you that your vehicle's {doc} "\
              f"certificate is going to expire soon.\n"\
              f"Kindly get it renewed to avoid unnecessary traffic fines.\n"\
              f"Thanking you!\n"\
              f"Traffic Police"
    subject = f"Reminder: The {doc} certificate of vehicle "\
              f"({vehicle_no}) is going to expire."
    if over_due:
        message = message.replace(
            'is going to expire soon.',
            'has expired. Driving without proper documents is traffic violation.')
        subject = subject.replace('is going to expire', 'has expired')
    return dict(
        subject=subject,
        message=message)


def send_email_due():
    from application.models import Vehicle
    today = datetime.datetime.now().date()

    for vehicle in Vehicle.objects.all():
        for doc in (
                ('pollution', vehicle.pollution_date),
                ('insurance', vehicle.insurance_date)):
            two_before_date = doc[1] - datetime.timedelta(2)
            # Two Days before due date
            if two_before_date <= today and today < doc[1]:
                print('Due: ', vehicle.owner.first_name)

                def mail_user(): return send_mail(
                    **email_details(
                        name=vehicle.owner.first_name,
                        vehicle_no=vehicle.vehicle_no,
                        over_due=False, doc=doc[0]),
                    from_email='testpython06@gmail.com',
                    recipient_list=[vehicle.owner.email, ],
                    fail_silently=False,
                )
                # mail_user()
                # timethread(mail_user, join=True)
            elif today >= doc[1]:
                print('Overdue: ', vehicle.owner.first_name)

                def mail_user(): return send_mail(
                    **email_details(
                        name=vehicle.owner.first_name,
                        vehicle_no=vehicle.vehicle_no,
                        over_due=False, doc=doc[0]),
                    from_email='testpython06@gmail.com',
                    recipient_list=[vehicle.owner.email, ],
                    fail_silently=True,
                )
                # mail_user()
                # timethread(mail_user, join=True)


year = datetime.datetime.now().year
last_date = datetime.date(year, 12, 31)

@run_once
@timethread(date_time=last_date, time_interval=1000, quiet=True)
def rank_at_end():
    from application.models import (Profile, Complaint,
                                    PoliceStation)
    
    for profile in Profile.objects.all():
        if profile.rank == 500:
            print('Bonus', profile.user)
            Complaint(
                user=profile.user,
                complaint_type='Bonus',
                police_station=PoliceStation.objects.all()[0],
                complaint="Congratulations! For not violating "
                          "any traffic laws in a year.",
                challan_amount=2000,
                status='Approved',
            ).save()
        elif profile.rank < 400:
            print('Penalty', profile.user)
            Complaint(
                user=profile.user,
                complaint_type='Penalty',
                police_station=PoliceStation.objects.all()[0],
                complaint="Penalty! For violating traffic "
                          "laws too many times in a year.",
                challan_amount=2000,
                status='Due',
            ).save()


class ApplicationConfig(AppConfig):
    name = 'application'

    def ready(self):
        send_email_due()
        rank_at_end()
