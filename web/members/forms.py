from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name','last_name','email' ]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        # fields = '__all__'

class ProfileOtherUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = ['birthday','age']
        fields = '__all__'

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)


