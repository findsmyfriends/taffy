from django import forms
from django.contrib.auth.models import Permission, User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import fields
from .models import  Match, Member, Profile, Rating
from django.forms import DateInput
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput

class DateInput(forms.DateInput):
    input_type = 'date'
    input_formats=['%d-%m-%Y'], 

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = Member
        fields = ['username', 'first_name','last_name','email', 'birthday','password1', 'password2']
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Member
        fields = ['username', 'email','first_name','last_name']

class UserFilterUpdateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name','last_name']

class ProfileFilterUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birthday','bloodtype','image',]
        widgets = {
        'birthday': DateInput(),
        }
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birthday','age','gender','testes','daysofweek','rasi','bloodtype','naksus','image']
        widgets = {
        # 'birthday': DateInput(attrs={'type': 'date'}, format='%YYYY/%mm/%d'),
        'birthday': DateInput(),
        }
   

class ProfileDetailFrom(forms.ModelForm):
   
        model = Profile
        fields = '__all__'
    
class MessageForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='')

class RatingForm(forms.Form):
    model = Rating
    fields = ['ratingUser']

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        # fields =['user2']
        fields = '__all__'

