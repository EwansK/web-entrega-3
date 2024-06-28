from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer

class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '**************'}))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '**************'}))
    birthdate = forms.DateField(label='Fecha de Nacimiento', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'id_number', 'email', 'phone', 'password1', 'password2', 'birthdate']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rut'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@gmail.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+56912345678'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')

        return cleaned_data

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'id_number', 'email', 'phone', 'date_of_birth']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rut'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@gmail.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+56912345678'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
