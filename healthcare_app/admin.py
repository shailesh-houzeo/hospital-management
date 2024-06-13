from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import (
    Patient, Doctor, Appointment, MedicalRecord, Prescription, Payment, 
    RadiologyTest, PathologyTest, Vaccination, MedicalClaim, Consultant, 
    Billing, InventoryItem, DoctorInformation, DischargeSummary, PharmacyItem
)

class PatientAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'name', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'name')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('name', 'email', 'age', 'gender', 'phone_number', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'name', 'age', 'gender', 'phone_number', 'address', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization')
    search_fields = ('first_name', 'last_name', 'specialization')
    ordering = ('last_name',)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date_time', 'status')
    search_fields = ('patient__username', 'doctor__first_name', 'doctor__last_name')
    list_filter = ('status', 'date_time')
    ordering = ('date_time',)

class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'blood_type')
    search_fields = ('patient__username', 'blood_type')
    ordering = ('patient__username',)

class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'medication', 'dosage', 'frequency')
    search_fields = ('appointment__patient__username', 'medication')
    ordering = ('appointment__date_time',)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'amount', 'date_paid')
    search_fields = ('appointment__patient__username',)
    ordering = ('date_paid',)

class RadiologyTestAdmin(admin.ModelAdmin):
    list_display = ('patient', 'test_name', 'test_date')
    search_fields = ('patient__username', 'test_name')
    ordering = ('test_date',)

class PathologyTestAdmin(admin.ModelAdmin):
    list_display = ('patient', 'test_name', 'test_date')
    search_fields = ('patient__username', 'test_name')
    ordering = ('test_date',)

class VaccinationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'vaccine_name', 'administered_date')
    search_fields = ('patient__username', 'vaccine_name')
    ordering = ('administered_date',)

class MedicalClaimAdmin(admin.ModelAdmin):
    list_display = ('patient', 'claim_date', 'amount_claimed', 'is_approved')
    search_fields = ('patient__username',)
    ordering = ('claim_date',)

class ConsultantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization', 'phone_number', 'email')
    search_fields = ('first_name', 'last_name', 'specialization')
    ordering = ('last_name',)

class BillingAdmin(admin.ModelAdmin):
    list_display = ('patient', 'amount', 'date_billed', 'is_paid')
    search_fields = ('patient__username',)
    ordering = ('date_billed',)

class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'quantity')
    search_fields = ('item_name',)
    ordering = ('item_name',)

class DoctorInformationAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'qualifications', 'experience')
    search_fields = ('doctor__first_name', 'doctor__last_name', 'qualifications')
    ordering = ('doctor__last_name',)

class DischargeSummaryAdmin(admin.ModelAdmin):
    list_display = ('patient', 'discharge_date')
    search_fields = ('patient__username',)
    ordering = ('discharge_date',)

class PharmacyItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'price')
    search_fields = ('item_name',)
    ordering = ('item_name',)

admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(MedicalRecord, MedicalRecordAdmin)
admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(RadiologyTest, RadiologyTestAdmin)
admin.site.register(PathologyTest, PathologyTestAdmin)
admin.site.register(Vaccination, VaccinationAdmin)
admin.site.register(MedicalClaim, MedicalClaimAdmin)
admin.site.register(Consultant, ConsultantAdmin)
admin.site.register(Billing, BillingAdmin)
admin.site.register(InventoryItem, InventoryItemAdmin)
admin.site.register(DoctorInformation, DoctorInformationAdmin)
admin.site.register(DischargeSummary, DischargeSummaryAdmin)
admin.site.register(PharmacyItem, PharmacyItemAdmin)
