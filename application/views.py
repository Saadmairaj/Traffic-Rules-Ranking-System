import datetime
# from pyexpat.errors import messages
from django.contrib import messages
from django.db import transaction
from django.conf import settings
from django.db.models import Q
from django.contrib.auth.models import User
from django.template.response import TemplateResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.views.generic import CreateView, TemplateView, ListView, UpdateView
from django.views.generic.edit import FormView

from application.forms import ComplaintForm, ComplaintPaymentForm, ProfileForm, UserForm, SignUpForm, ContactForm
from application.models import Complaint, PoliceStation, Vehicle, Profile

from payments import get_payment_model, RedirectNeeded


def payment_details(request, payment_id):
    payment = get_object_or_404(get_payment_model(), id=payment_id)
    try:
        form = payment.get_form(data=request.POST or None)
    except RedirectNeeded as redirect_to:
        return redirect(str(redirect_to))
    return TemplateResponse(request, 'payment.html',
                            {'form': form, 'payment': payment})


def signup(request):
    """
    Sign up
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


@login_required(login_url='/login/')
def change_password(request):
    """
    Change Password
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {
        'form': form
    })


@login_required
@transaction.atomic
def update_profile(request):
    """
    Update Profile
    :param request:
    :return:
    """
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'account/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
def view_profile(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'view-profile.html', {
        'user': user,
        'user_form': UserForm(instance=user),
        'profile_form': ProfileForm(instance=user.profile)
    })


class HomePageView(TemplateView):
    """
    Home Page
    """
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class ContactView(FormView):
    """
    Contact Us Page
    """
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ComplaintView(FormView):
    model = Complaint
    form_class = ComplaintForm
    template_name = 'complaint.html'
    success_url = '/thanks/'

    def form_valid(self, form, *args, **kwargs):
        obj = form.save(commit=False)
        obj.user = User.objects.filter(
            username=form.cleaned_data['user']).first()
        obj.police_station = PoliceStation.objects.filter(
            station_city=form.cleaned_data['police_station']).first()
        obj.status = form.cleaned_data['status']
        obj.complaint_type = form.cleaned_data['complaint_type']
        obj.save()
        obj.send_email()
        return super(ComplaintView, self).form_valid(form)


class ComplaintListView(ListView):
    paginate_by = settings.ITEMS_PER_PAGE
    model = Complaint
    fields = ['user', 'complaint_type', 'police_station', 'complaint',
              'challan_amount', 'status', 'resolved_date', 'resolved_message']
    template_name = 'complaint-list.html'
    context_object_name = 'complaints'

    def get_context_data(self, **kwargs):
        context = super(ComplaintListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self, **kwargs):
        queryset = Complaint.objects.filter().order_by('-id')

        group = self.request.user.groups.values_list('name', flat=True).first()
        if group == "Police":
            queryset = queryset.filter(
                Q(police_station=self.request.user.profile.police_station) |
                Q(user=self.request.user)
            )
        else:
            queryset = queryset.filter(user=self.request.user)

        query = self.request.GET.get('q')
        if query:
            # Filter by first name, last name, email, licence_no.
            query_fields = [Q(**{f: query}) for f in (
                'user__username',
                'complaint__icontains',
                'complaint_type__iexact',
                'status__iexact'
            )]
            q = query_fields[0]
            for f in query_fields:
                if 'user__username' in f.children[0] and group == 'General':
                    continue
                q |= f
            try:
                queryset = queryset.filter(q).distinct()
            except (ValueError, ) as err:
                print(err)

        return queryset


class ComplaintChallan(CreateView):
    model = Complaint
    fields = ['police_station', 'complaint', 'challan_amount']
    template_name = 'complaint-challan.html'
    success_url = '/thanks/'

    def render_to_response(self, context, **response_kwargs):
        print(context, self.kwargs)
        context['challan_user'] = User.objects.get(pk=self.kwargs.get('pk'))
        return super().render_to_response(context, **response_kwargs)

    def form_valid(self, form, *args, **kwargs):
        obj = form.save(commit=False)
        obj.user = User.objects.get(pk=self.kwargs.get('pk'))
        obj.complaint_type = 'Challan'
        obj.status = 'Due'
        obj.save()
        obj.send_email(challan=True)
        return super(ComplaintChallan, self).form_valid(form)


class ComplaintUpdateView(UpdateView):
    model = Complaint
    fields = ['status', 'resolved_message', 'challan_amount']
    template_name = 'complaint.html'
    success_url = '/thanks/'

    def form_valid(self, form, *args, **kwargs):
        obj = form.save(commit=False)
        obj.resolved_by = self.request.user
        obj.resolved_date = datetime.datetime.now()
        obj.save()
        obj.send_email(resolved=True)
        return super(ComplaintUpdateView, self).form_valid(form)


class VehiclesListView(ListView):
    paginate_by = settings.ITEMS_PER_PAGE
    model = Vehicle
    fields = '__all__'
    template_name = 'vehicle-list.html'
    context_object_name = 'vehicles'

    def get_context_data(self, **kwargs):
        context = super(VehiclesListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self, **kwargs):
        queryset = self.model.objects.filter(
        ).order_by('-date_created')
        group = self.request.user.groups.all()
        if "Police" not in group:
            queryset = queryset.filter(owner=self.request.user)
        query = self.request.GET.get('q')
        if query:
            # Filter by first name, last name, email, licence_no.
            query_fields = [Q(**{f: query}) for f in (
                'owner__username',
                'fuel_type__icontains',
                'manufacute_year',
                # 'company',
                'vehicle_no__icontains'
            )]
            q = query_fields[0]
            for f in query_fields:
                q |= f
            try:
                queryset = queryset.filter(q).distinct()
            except (ValueError, ) as err:
                print(err)
        return queryset


class ProfilesListView(ListView):
    paginate_by = settings.ITEMS_PER_PAGE
    model = Profile
    fields = '__all__'
    template_name = 'profile-list.html'
    context_object_name = 'profiles'

    def get_queryset(self, **kwargs):
        queryset = self.model.objects.filter(
        ).order_by('-user__date_joined')

        query = self.request.GET.get('q')
        if query:

            # Filter by first name, last name, email, licence_no.
            query_fields = [Q(**{f: query}) for f in (
                'user__username',
                'user__first_name__iexact',
                'user__last_name__iexact',
                'user__email__iexact',
                'user__email__icontains',
                'drivers_licence_no__iexact',
                'city__iexact'
                # 'rank',
            )]

            # Filter by groups (status)
            groups = {'police': 1, 'general': 2}
            if query in groups:
                query_fields += [Q(user__groups=groups[query.lower()])]

            q = query_fields[0]
            for f in query_fields:
                q |= f
            try:
                queryset = queryset.filter(q).distinct()
            except (ValueError, ) as err:
                print(err)
        return queryset


class PaymentView(UpdateView):
    model = Complaint
    form_class = ComplaintPaymentForm
    template_name = 'payment.html'
    success_url = '/thanks/'

    def form_valid(self, form, *args, **kwargs):
        obj = form.save(commit=False)
        obj.resolved_by = self.request.user
        obj.resolved_date = datetime.datetime.now()
        obj.status = 'Paid'
        obj.save()
        obj.send_email(challan=True)
        return super(PaymentView, self).form_valid(form)
