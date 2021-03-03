from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from application.models import Profile


class SignUpForm(UserCreationForm):
    #first_name = forms.CharField(max_length=50, required=True)
    #last_name = forms.CharField(max_length=50, required=True)
    #email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    # first_name = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Username'
    #     }
    # ))
    # password1 = forms.CharField(widget=forms.PasswordInput(
    #     attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Password'
    #     }
    # ))
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
