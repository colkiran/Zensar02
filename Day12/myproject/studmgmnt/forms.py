
from django.core import validators
from django import forms
from .models import Stud
#
class StudRegistration(forms.ModelForm):
    class Meta:
        model = Stud
        fields = ['stud_name', 'stud_dob', 'stud_class']
        widgets = {
            'stud_name': forms.TextInput(attrs={'class': 'form-control'}),
            'stud_dob': forms.TextInput(attrs={'class': 'form-control'}),
            'stud_class': forms.TextInput(attrs={'class': 'form-control'})
        }