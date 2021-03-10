import datetime
from pyexpat.errors import messages
from django.db import transaction
from django.db.models import Q
from django.contrib.auth.models import User
from django.template.response import TemplateResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.views.generic import CreateView, TemplateView, ListView, UpdateView

from application.forms import ProfileForm, UserForm, SignUpForm
from application.models import Contact, Complaint, Vehicle, Profile

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
            # messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        # else:
        #     print("aaaaaaaaa")
            #messages.error(request, 'Please correct the error below.')
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


class ContactView(CreateView):
    """
    Contact Us Page
    """
    model = Contact
    fields = ['name', 'email', 'mobile', 'message']
    template_name = 'contact.html'
    success_url = '/thanks/'


class ComplaintView(CreateView):
    model = Complaint
    fields = ['complaint_type', 'police_station', 'user',
              'complaint', 'challan_amount', 'status']
    template_name = 'complaint.html'
    success_url = '/thanks/'

    def form_valid(self, form, *args, **kwargs):
        obj = form.save(commit=False)
        obj.save()
        obj.send_email()
        return super(ComplaintView, self).form_valid(form)


class ComplaintListView(ListView):
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
                police_station=self.request.user.profile.police_station)
        else:
            queryset = queryset.filter(user=self.request.user)
        return queryset


class VehiclesListView(ListView):
    model = Vehicle
    fields = '__all__'
    template_name = 'vehicle-list.html'
    context_object_name = 'vehicles'

    def get_context_data(self, **kwargs):
        context = super(VehiclesListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self, **kwargs):
        queryset = Vehicle.objects.filter().order_by('-id')
        group = self.request.user.groups.values_list(
            'name', flat=True).first()
        if group == "Police":
            print("no any action")
        else:
            queryset = queryset.filter(owner=self.request.user)
        return queryset


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


class ProfilesListView(ListView):
    model = Profile
    fields = '__all__'
    template_name = 'profile-list.html'
    context_object_name = 'profiles'

    def get_queryset(self, **kwargs):
        query_list = self.model.objects.filter(
            ).order_by('-user__date_joined')

        query = self.request.GET.get('q')
        if query:
            query_fields = [Q(**{f: str(query)}) for f in (
                # 'user__username',
                'user__first_name__iexact', 
                'user__last_name__iexact',
                'user__email__iexact', 
                'user__email__icontains', 
                'drivers_licence_no__iexact',
                # 'rank',
                )   ]
            query_fields += [Q(user__groups=1 if query in 'police' else 2)]

            q = query_fields[0]
            for f in query_fields:
                q |= f
            try:
                query_list = query_list.filter(
                    q
                ).distinct()
            except (ValueError, ) as err: 
                print(err)
        return query_list


class PaymentView(UpdateView):
    model = Complaint
    fields = ['challan_amount', 'status']
    template_name = 'payment.html'
    success_url = '/thanks/'

    def form_valid(self, form, *args, **kwargs):
        obj = form.save(commit=False)
        obj.save()
        obj.resolved_by = self.request.user
        obj.resolved_date = datetime.datetime.now()
        obj.status = 'Paid'
        obj.send_email(challan=True)
        return super(PaymentView, self).form_valid(form)
