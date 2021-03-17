if __name__ == '__main__':
    import os
    os.system('export PYTHONPATH=.')
    # export DJANGO_SETTINGS_MODULE=trafficrule.settings

from os import name
import random
import datetime
import string

from django.utils import timezone
from django.contrib.auth.models import Group, User
from application.models import Company, Complaint, PoliceStation, Profile, Vehicle


class _Person:

    def __init__(self, police=False):

        # Initializing
        self._first_name = ''
        self._last_name = ''
        self._state = ''
        self._city = ''
        self._address = ''
        self._dob = ''
        self._country = ''
        self._rcode = ''
        self._licence = ''
        self._licence_validity = ''
        self._user = ''
        self._status = ''
        self._police = police

    @property
    def user(self):
        if getattr(self, '_user', '') == '':
            users = list(User.objects.values_list(
                'username', flat=True))
            for i in users.copy():
                if not i.startswith(self.rcode):
                    users.remove(i)
            users = sorted(users)
            if not users:
                self._user = self.rcode + '001' + self.status[0]
            else:
                count = len(users)
                while True:
                    num = str(count + 1)
                    if len(num) < 3:
                        num = ('0'*int(3-len(num))) + num
                    self._user = "%s%s%s" % (self.rcode, num, self.status[0])
                    if self._user not in users:
                        break
                    users = list(User.objects.values_list(
                        'username', flat=True))
                    count += 1
        return self._user

    @property
    def status(self):
        if self._police:
            return 'Police'
        return 'General'

    @property
    def first_name(self):
        if getattr(self, '_first_name', '') == '':
            with open('populate_db/firstnames.txt', 'r') as file:
                names = file.read().split('\n')
            self._first_name = random.choice(names).capitalize()
        return self._first_name

    @property
    def last_name(self):
        if getattr(self, '_last_name', '') == '':
            with open('populate_db/lastnames.txt', 'r') as file:
                names = file.read().split('\n')
            self._last_name = random.choice(names).capitalize()
        return self._last_name

    @property
    def name(self):
        return "%s %s" % (self.first_name, self.last_name)

    @property
    def email(self):
        return str(
            "%s%s@gamil.com" % (self.first_name, self.last_name)
        ).lower()

    @property
    def dob(self, age_greater=40):
        year = random.randint(
            2021-age_greater-int(age_greater/2), 2021-age_greater)
        month = random.randint(1, 12)
        date = random.randint(1, 26)
        hour = random.randint(1, 23)
        minutes = random.randint(1, 59)
        seconds = random.randint(1, 59)
        return datetime.datetime(
            year, month, date, hour, minutes, seconds,
            tzinfo=timezone.utc)

    @property
    def gender(self, auto=True):
        """Returns random gender (male/female). 
        "Auto" functionality is experimental and 
        may not work as intended."""
        if auto:
            if (self.first_name.endswith('a')
                or self.first_name.endswith('ine')
                    or self.first_name.endswith('ie')):
                return 'Female'
            return 'Male'
        return random.choice(['Male', 'Female'])

    @property
    def address(self):
        home = ' '.join(
            [random.choice(['Flat', 'House', 'Apartment']),
             'no:', str(random.randint(1, 500))])
        area = 'Somewhere On Earth'
        return "%s, %s, %s, %s, %s" % (
            home, area, self.state, self.city, self.pin)

    @property
    def state(self):
        if getattr(self, '_state', '') == '':
            with open('populate_db/cities.txt', 'r') as file:
                city_state = random.choice(file.read().split('\n'))
                self._city, self._state, self._rcode = [
                    str(i).capitalize() for i in city_state.split(', ')]
        return self._state

    @property
    def rcode(self):
        if getattr(self, '_rcode', '') == '':
            with open('populate_db/cities.txt', 'r') as file:
                city_state = random.choice(file.read().split('\n'))
                self._city, self._state, self._rcode = [
                    str(i).capitalize() for i in city_state.split(', ')]
        return self._rcode.upper()

    @property
    def city(self):
        if getattr(self, '_city', '') == '':
            with open('populate_db/cities.txt', 'r') as file:
                city_state = random.choice(file.read().split('\n'))
                self._city, self._state, self._rcode = [
                    str(i).capitalize() for i in city_state.split(', ')]
        return self._city

    @property
    def country(self):
        return 'India'

    @property
    def pin(self):
        return int(''.join(
            [str(i) for i in random.choices(
                range(1, 10), k=6)]
        ))

    @property
    def mobile(self):
        initials = str(random.choice([91, 88, 72, 99, 92, 70, 98]))
        return '+91 ' + initials + str(random.choice(range(10000000, 99999999)))

    @property
    def licence(self):
        if getattr(self, '_licence', '') == '':
            all_licence = Profile.objects.values_list(
                'drivers_licence_no', flat=True)
            while True:
                num = str(random.randint(10000000000, 100000000000-1))
                init = str(random.randint(10, 40))
                self._licence = "%s%s-%s" % (self.rcode, init, num)
                if self._licence not in all_licence:
                    break
        return self._licence

    @property
    def licence_validity(self):
        if getattr(self, '_licence_validity', '') == '':
            year = self.dob.year + 40
            self._licence_validity = datetime.date(
                year=random.choice(range(year+20, year+30)),
                month=random.choice(range(1, 12)),
                day=random.choice(range(1, 26)))
        return self._licence_validity

    @property
    def licence_imagepath(self):
        if self.gender == 'female':
            return 'Assets/template_license_f.pdf'
        return 'Assets/template_license.pdf'

    def complete_details_pprint(self):
        out = "\nFirst name:      %s" % self.first_name + \
            "\nLast name:       %s" % self.last_name + \
            "\nEmail:           %s" % self.email + \
            "\nMobile:          %s" % self.mobile + \
            "\nDOB:             %s" % self.dob + \
            "\nAddress:         %s" % self.address + \
            "\nGender:          %s" % self.gender
        return out


class _Vehicle:

    def __init__(self):
        self._user = ''
        self._vehicle_no = ''
        self._registration_date = ''
        self._rc = ''

        self._pollution = ''
        self._pollution_date = ''

        self._insurance = ''
        self._insurance_no = ''
        self._insurance_date = ''

    @property
    def owner(self):
        if getattr(self, '_user', '') == '':
            self._user = random.choice(User.objects.filter())
        return self._user

    @property
    def vehicle_number(self):
        if getattr(self, '_vehicle_no', '') == '':
            with open('populate_db/cities.txt', 'r') as file:
                code = random.choice(file.read().split('\n'))
                code = code.split(', ')[-1] + str(random.randint(10, 99))
                self._vehicle_no = code + ''.join(
                    random.choices(string.ascii_uppercase, k=3)
                ) + str(random.randint(1000, 9999))
        return self._vehicle_no

    @property
    def fuel_type(self):
        if getattr(self, '_fuel', '') == '':
            self._fuel = random.choice(Vehicle.FUEL)[0]
        return self._fuel

    @property
    def model(self):
        if getattr(self, '_model', '') == '':
            self._model = ''.join(random.choices(
                string.ascii_lowercase, k=random.randint(3, 8))
            ).capitalize() + ' ' + ''.join(random.choices(
                string.ascii_uppercase, k=random.randint(2, 3)))
        return self._model

    @property
    def company(self):
        if getattr(self, '_company', '') == '':
            self._company = random.choice(
                Company.objects.filter())
        return self._company

    @property
    def registered_address(self):
        return Profile.objects.filter(
            user=self.owner).values_list(
                'address', flat=True)[0]

    @property
    def registered_district(self):
        return Profile.objects.filter(
            user=self.owner).values_list(
                'state', flat=True)[0]

    registered_state = registered_district

    @property
    def registration_date(self):
        if getattr(self, '_registration_date', '') == '':
            old = 7
            self._registration_date = datetime.datetime(
                year=random.randint(2021-7, 2020),
                month=random.randint(1, 12),
                day=random.randint(1, 20),
                tzinfo=timezone.utc,
            )
        return self._registration_date

    @property
    def insurance_no(self):
        if getattr(self, '_insurance_no', '') == '':
            self._insurance_no = ''.join(
                [str(i) for i in random.choices(range(10), k=10)])
        return self._insurance_no

    @property
    def pollution_date(self):
        if getattr(self, '_pollution_date', '') == '':
            self._pollution_date = datetime.date(
                year=random.choice([2021, 2022]),
                month=random.randint(1, 12),
                day=random.randint(1, 25),
            )
        return self._pollution_date

    @property
    def insurance_date(self,):
        if getattr(self, '_insurance_date', '') == '':
            self._insurance_date = datetime.date(
                year=random.choice([2021, 2022]),
                month=random.randint(1, 12),
                day=random.randint(1, 25),
            )
        return self._insurance_date

    @property
    def manufacture_year(self):
        return self.registration_date.year


class _Company:
    companies = [
        "Maruti Suzuki",
        "Hyundai Motors",
        "Tata Motors",
        "Toyota",
        "Kia Motors",
        "Skoda",
        "MG",
        "Mercedes",
        "Volkswagen",
        "Honda",
        "Renault",
        "Mahindra",
        "BMW",
        "Jeep",
        "Ford",
        "Nissan",
        "Audi",
        "Datsun",
        "Tesla",
    ]

    @property
    def company_name(self):
        if getattr(self, '_name', '') == '':
            self._name = random.choice(self.companies)
        return self._name


class _PoliceStation:
    def _open_cities(self, attr):
        if getattr(self, attr, '') == '':
            with open('populate_db/cities.txt', 'r') as file:
                city_state = random.choice(file.read().split('\n'))
                self._city, self._state, self._rcode = [
                    str(i).capitalize() for i in city_state.split(', ')]
        return getattr(self, attr)

    @property
    def state(self):
        return self._open_cities('_state')

    @property
    def city(self):
        return self._open_cities('_city')

    @property
    def employees(self):
        return random.randint(10, 20)

    @property
    def station(self):
        if getattr(self, '_station', '') == '':
            with open('populate_db/randomlocations.txt', 'r') as file:
                locs = file.read().split('\n')
                while True:
                    self._station = 'Police Station ' + random.choice(locs)
                    stations = list(PoliceStation.objects.all(
                    ).values_list('station_city', flat=True))
                    if self._station not in stations:
                        break
        return self._station

    @property
    def pin(self):
        return int(''.join(
            [str(i) for i in random.choices(
                range(1, 10), k=6)]
        ))

    @property
    def address(self):
        home = ' '.join(
            [random.choice(['Flat', 'House', 'Apartment']),
             'no:', str(random.randint(1, 500))])
        return "%s, %s, %s, %s, %s" % (
            home, self.station, self.state, self.city, self.pin)

    @property
    def date_created(self):
        return datetime.date(
            year=random.randint(1800, 2010),
            month=random.randint(1, 12),
            day=random.randint(1, 26),
        )


class _Complaint:
    @property
    def user(self):
        if getattr(self, '_user', '') == '':
            self._user = random.choice(
                User.objects.filter())
        return self._user

    @property
    def type(self):
        if getattr(self, '_type', '') == '':
            # self._type = random.choice(Complaint.TYPE)[0]
            self._type = random.choice(['Challan', 'FIR'])
        return self._type

    @property
    def message(self):
        if getattr(self, '_message', '') == '' and self.type == 'Challan':
            with open('populate_db/violations.txt') as file:
                self._message, self._challan = random.choice(
                    file.read().split('\n')).split(';; ')
        elif getattr(self, '_message', '') == '':
            with open('populate_db/fircomplaints.txt') as file:
                self._message = random.choice(
                    file.read().split('\n'))
        return self._message

    @property
    def station(self):
        if getattr(self, '_station', '') == '':
            self._station = random.choice(
                PoliceStation.objects.filter())
        return self._station

    @property
    def challan(self):
        if getattr(self, '_challan', '') == '' and self.type == 'Challan':
            with open('populate_db/violations.txt') as file:
                self._message, self._challan = random.choice(
                    file.read().split('\n').split(';;'))
        elif self.type != 'Challan':
            self._challan = 0
        return self._challan

    @property
    def status(self):
        if getattr(self, '_status', '') == '' and self.type == 'Challan':
            self._status = 'Due'
        elif self.type != 'Challan':
            self._status = 'Pending'
        return self._status

    @property
    def date_created(self):
        if getattr(self, '_date_created', '') == '':
            year = random.randint(2021, 2021)
            month = random.randint(1, 12)
            if year == 2021:
                month = random.randint(1, 3)
            self._date_created = datetime.datetime(
                year=year,
                month=month,
                day=random.randint(1, 26),
                tzinfo=timezone.utc
            )
        return self._date_created



########################################################################
############################### POPULATE ###############################
########################################################################


def populateProfile(num='', police=False, police_station=None):
    person = _Person(police=True)
    print(num, person.user)

    # Creating new user
    user = User(
        username=person.user,
        first_name=person.first_name,
        last_name=person.last_name,
        email=person.email,
        date_joined=person.dob)
    user.set_password('test@123')
    user.save()

    # Adding new user to the group
    group = Group.objects.get(name=person.status)
    group.user_set.add(user)

    # Fetching the profile with new user.
    profile = Profile.objects.filter(user=user)

    # Adding infomation to the profile.
    if profile:
        profile = profile[0]
        profile.mobile = person.mobile
        profile.gender = person.gender
        profile.dob = person.dob
        profile.address = person.address
        profile.city = person.city
        profile.state = person.state
        profile.gender = person.gender
        profile.pin = person.pin
        profile.country = person.country
        profile.drivers_licence_no = person.licence
        profile.licence_valid_date = person.licence_validity
        profile.licence_issue_state = person.state
        profile.licence_img = person.licence_imagepath
        profile.save()

    return profile


def populateVehicle(num=''):
    vehicle = _Vehicle()
    print(num, vehicle.owner, vehicle.vehicle_number)

    ve = Vehicle(
        owner=vehicle.owner,
        vehicle_no=vehicle.vehicle_number,
        model_no=vehicle.model,
        fuel_type=vehicle.fuel_type,
        manufacute_year=vehicle.manufacture_year,
        company=vehicle.company,
        registered_address=vehicle.registered_address,
        registered_district=vehicle.registered_district,
        registered_state=vehicle.registered_state,
        date_created=vehicle.registration_date,
        # rc_img=,
        insurance_no=vehicle.insurance_no,
        # insurance_img=,
        insurance_date=vehicle.insurance_date,
        # pollution_img=,
        pollution_date=vehicle.pollution_date,
    )

    ve.save()
    return ve


def populateCompany(num=''):
    for i in _Company.companies:
        print(num, i)
        Company(
            company_name=i
        ).save()


def populatePolice(num=''):
    ps = _PoliceStation()
    users = []
    print(num, ps.station)

    for i in range(ps.employees):
        users.append(populateProfile(i, True))

    police_station = PoliceStation(
        station_incharge=random.choice(users).user,
        station_city=ps.station,
        address=ps.address,
        no_of_employee=ps.employees,
        date_created=ps.date_created
    )
    police_station.save()
    for user in users:
        user.police_station = police_station
        user.save()
    return ps


def populateComplaint(num=''):
    c = _Complaint()
    print(num, c.user, c.type)

    complaint = Complaint(
        user=c.user,
        complaint_type=c.type,
        police_station=c.station,
        complaint=c.message,
        challan_amount=c.challan,
        status=c.status,
        date_created=c.date_created,
    )
    complaint.save()
    return complaint



def delete_invalid_entries():
    pass


if __name__ == '__main__':
    vehicle = _Vehicle()
    print(vehicle.vehicle_number)
