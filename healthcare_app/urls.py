from django.urls import path
from . import views
from .views import CustomLoginView, CustomLogoutView
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', views.home, name='home'),
    path('patients/<str:username>/', views.patient_detail, name='patient_detail'),
    path('doctors/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    # path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),    
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('update_profile/', views.update_profile, name='update_profile'),
    
]
