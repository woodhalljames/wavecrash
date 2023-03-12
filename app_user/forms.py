from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'email' ,'password1', 'password2')

class AppUserForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ('gender', 'address', 'mobile', 'city', 'zipcode')

        widgets = {
            'mobile':forms.TextInput(attrs={'type':'tel',
                                            'pattern':'[0-9]{10}'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }