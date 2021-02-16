  
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from api.models import MemberProfile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        fields = '__all__'