from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

user = get_user_model()

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'LoginField'}))
    password1 = forms.CharField(label='Password1', widget=forms.PasswordInput(attrs={'class': 'PasswordField'}))
    password2 = forms.CharField(label='Password2', widget=forms.PasswordInput(attrs={'class': 'PasswordField'}))
    class Meta:
        model = user
        fields = ('username', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'LoginField'}),
            'password1': forms.PasswordInput(attrs={'class': 'PasswordField'}),
            'password2': forms.PasswordInput(attrs={'class': 'PasswordField'}),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'LoginField'}))
    password = forms.CharField(label='Password1', widget=forms.PasswordInput(attrs={'class': 'PasswordField'}))
    class Meta:
        model = user
        fields = ('username', 'password1')


class PersonEventForm(forms.ModelForm):
    class Meta(object):
        model = PersonEvent
        fields = ('title', 'logo', 'description', 'date', 'city', 'address')
        exclude = ('creater', )

        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

class TeamEventForm(forms.ModelForm):
    class Meta:
        model = TeamEvent
        fields = ('title', 'logo', 'description', 'date', 'city', 'address', 'cat')
        exclude = ('creater', )

        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

class TeamForm(forms.ModelForm):
    class Meta(object):
        model = Team
        exclude = ('admin',)

class profileEditForm(forms.Form):
    username = forms.CharField(max_length=255)
    status = forms.CharField(widget=forms.Textarea())
    city = forms.CharField(max_length=255)