from django.forms import ModelForm
from .models import UserInformation
from django import forms

class Userform(ModelForm):
    class Meta:
        model = UserInformation
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'last_name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}),
            'Cnic_number': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control'}),
        }
        # attrs = {'class': 'modal-content'}
