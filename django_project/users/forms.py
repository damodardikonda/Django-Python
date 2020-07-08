from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile


class UserRegisterationForms(UserCreationForm):
    email=forms.EmailField()


    class Meta:# it saves Configuration at one place
        model=User #User because whenever form is validate it creates an user....
        fields=['username','email','password1','password2'] # we want to print this fields on forms


class UserUpdateForm(forms.ModelForm):# it only allow us to update username and email..
    email=forms.EmailField()


    class Meta:
        model=User
        fields=['username','email']


class ProfileUpdateForm(forms.ModelForm):


     class Meta:
         model=profile
         fields=['image']
