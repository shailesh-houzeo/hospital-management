from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Patient, Doctor, Appointment
from django.shortcuts import render, redirect
from .forms import PatientForm, DoctorForm, AppointmentForm
from django.contrib.auth import login
from .forms import PatientRegistrationForm, PatientLoginForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

@login_required
def patient_dashboard(request):
    return render(request, 'healthcare_app/patient_dashboard.html')

@login_required
def doctor_dashboard(request):
    return render(request, 'healthcare_app/doctor_dashboard.html')


def home(request):
    return render(request, 'healthcare_app/home.html')

def patient_detail(request, username):
    patient = get_object_or_404(Patient, username=username)
    return render(request, 'healthcare_app/patient_detail.html', {'patient': patient})

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    return render(request, 'healthcare_app/doctor_detail.html', {'doctor': doctor})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'healthcare_app/appointment_list.html', {'appointments': appointments})

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PatientForm()
    return render(request, 'healthcare_app/add_patient.html', {'form': form})

def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DoctorForm()
    return render(request, 'healthcare_app/add_doctor.html', {'form': form})

def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AppointmentForm()
    return render(request, 'healthcare_app/add_appointment.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = PatientRegistrationForm()
    return render(request, 'healthcare_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = PatientLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('patient_dashboard')
    else:
        form = PatientLoginForm()
    return render(request, 'healthcare_app/login.html', {'form': form})

@login_required
def patient_dashboard(request):
    patient = request.user
    appointments = Appointment.objects.filter(patient=patient)
    return render(request, 'healthcare_app/patient_dashboard.html', {'patient': patient, 'appointments': appointments})

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = PatientProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('patient_dashboard')
    else:
        form = PatientProfileForm(instance=request.user)
    return render(request, 'healthcare_app/update_profile.html', {'form': form})


class CustomLoginView(auth_views.LoginView):
    template_name = 'healthcare_app/login.html'

class CustomLogoutView(auth_views.LogoutView):
    template_name = 'healthcare_app/logout.html'