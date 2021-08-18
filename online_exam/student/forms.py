from django import forms
from django.contrib.auth.models import User
#from . import models
from .models import Student
#from quiz import models as QMODEL

class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['address','mobile','profile_pic']

