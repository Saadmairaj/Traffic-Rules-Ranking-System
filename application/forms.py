from django import forms
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from application.models import Complaint, Profile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('mobile', 'gender', 'dob', 'address',
                  'city', 'state', 'pin', 'country', 'drivers_licence_no',
                  'licence_img')


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    mobile = forms.IntegerField(required=True)
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        message = "Your query has been registered." \
                  " Someone from our team will contact" \
                  " you on your registerted mobile" \
                  " number {} at earliest."\
                  .format(self.cleaned_data['mobile'])

        return send_mail(
            subject="Thanks for Contacting us!",
            message=message,
            from_email='testpython06@gmail.com',
            recipient_list=[self.cleaned_data['email'], ],
            fail_silently=False)


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['complaint', 'challan_amount']

    user = forms.CharField(max_length=100, widget=forms.TextInput)
    status = forms.CharField(max_length=100, widget=forms.TextInput)
    complaint_type = forms.CharField(max_length=100, widget=forms.TextInput)
    police_station = forms.CharField(max_length=100, widget=forms.TextInput)


class ComplaintPaymentForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['challan_amount', 'status']

    status = forms.CharField(disabled=True)
    challan_amount = forms.CharField(disabled=True)
