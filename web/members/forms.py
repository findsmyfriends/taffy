from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.forms import fields, widgets
from .models import Match, Member, Profile


class DateInput(forms.DateInput):
    input_type = 'date'
    input_formats = ['%d-%m-%Y'],


class MemberLoginForm(UserCreationForm):
    class Meta:
        model = Member
        fields = ['username', 'password']
        widgets = {
            'password': forms.TextInput(attrs={'class': 'form-controls', 'type': 'password', 'name': 'password'}),
        }


class MemberRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Member
        fields = ['username', 'email', 'password1', 'password2', 'first_name',
                  'last_name', 'profile_image', 'birthday', 'bloodtype', 'gender', 'testes', ]
#
        widgets = {


            # 'profile_image':forms.TextInput(attrs={'class':'form-controls-file','type':'file',}),
            'gender': forms.TextInput(attrs={'class': 'form-check-input', 'type': 'radio', 'name': 'gender'}),
            'testes': forms.TextInput(attrs={'class': 'form-check-input', 'type': 'radio', 'neme': 'testes'}),
            'birthday': DateInput(attrs={'class': 'form-control', 'type': 'date', 'value': '11-03-1998', 'id': 'birthday', 'name': 'birthday'}),

        }


class MemberSettingUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Member
        fields = ['username', 'email', 'testes', 'phone_number']


class MemberProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name',
                  'birthday', 'bloodtype', 'profile_image', 'testes', 'gender', 'description', ]
        #
        widgets = {
            'gender': forms.TextInput(attrs={'class': 'form-check-input', 'type': 'radio', 'name': 'gender', 'id': 'id_gender'}),
            'testes': forms.TextInput(attrs={'class': 'form-check-input', 'type': 'radio', 'neme': 'testes', 'id': 'id_testes'}),
            'birthday': DateInput(attrs={'class': 'form-control', 'type': 'date', 'value': '11-03-1998', 'id': 'birthday', 'name': 'birthday'}),
        }


class AccountDeleteForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = []


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Member
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = ['image']
        fields = '__all__'


# class ProfileOtherUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['gender','testes','birthday','age','rasi','bloodtype','naksus']
        # fields = '__all__'

class MessageForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='')


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = '__all__'

        # fields = fields = ['member1', 'member2', 'ratingPoint']
