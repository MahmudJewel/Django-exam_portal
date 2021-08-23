from django import forms
from django.contrib.auth.models import User
from . import models

class TeacherSalaryForm(forms.Form):
    salary=forms.IntegerField()