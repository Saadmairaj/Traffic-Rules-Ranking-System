from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from application.models import Profile, PoliceStation, Complaint, Company, Vehicle


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'
    readonly_fields = ('total_challan', 'rank')


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff',
                    'is_active')
    list_per_page = 20

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


@admin.register(PoliceStation)
class PoliceStationAdmin(admin.ModelAdmin):
    list_display = ('station_city', 'address', 'no_of_employee',
                    'date_created', 'date_updated')
    search_fields = ('station_city',)
    list_filter = ('station_city', 'date_created',)
    list_per_page = 20


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('complaint_type', 'user', 'police_station',
                    'complaint', 'status', 'date_created')
    search_fields = ('complaint_type', 'complaint')
    list_filter = ('complaint_type', 'status', 'date_created',)
    list_per_page = 20


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_website', 'company_address')
    search_fields = ('company_name', 'company_website')
    #list_filter = ('compnay_name', 'status', 'date_created',)
    list_per_page = 20


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('owner', 'vehicle_no', 'model_no',
                    'company', 'registered_state', 'date_created')
    search_fields = ('owner', 'vehicle_no', 'model_no')
    list_filter = ('date_created',)
    list_per_page = 20


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
