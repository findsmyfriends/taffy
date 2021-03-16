from django import forms
from django.contrib.auth.models import Permission, User
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
        fields = ['username', 'email','first_name','last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birthday','age','gender','testes','daysofweek','rasi','bloodtype','naksus','image']
        # fields = '__all__'

class ProfileDetailFrom(forms.ModelForm):
   
        model = Profile
        fields = '__all__'

class MessageForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='')

class RatingForm(forms.Form):
    pass



