from django import forms
from .models import Employee
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['phone','adress','profile_pic']



class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','password1','password2']