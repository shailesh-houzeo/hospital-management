from django import forms
from .models import Patient, Doctor, Appointment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['username', 'email', 'password', 'name', 'age', 'gender', 'phone_number', 'address']
        widgets = {
            'password': forms.PasswordInput(),
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'specialization', 'bio']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'date_time', 'reason', 'status']

class PatientRegistrationForm(UserCreationForm):
    class Meta:
        model = Patient
        fields = ['username', 'email', 'name', 'age', 'gender', 'phone_number', 'address', 'password1', 'password2']

class PatientLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['username', 'email', 'name', 'age', 'gender', 'phone_number', 'address']

