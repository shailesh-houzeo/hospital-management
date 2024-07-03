from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class PatientManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)


class Patient(AbstractUser, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True, blank=True)
    is_patient = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = PatientManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'age', 'gender', 'phone_number', 'address']

    def __str__(self):
        return self.username


class Doctor(models.Model):
    user = models.OneToOneField(Patient, on_delete=models.CASCADE)
    SPECIALIZATION_CHOICES = (
        ('GP', 'General Practitioner'),
        ('SP', 'Specialist'),
        ('SU', 'Surgeon'),
    )
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=2, choices=SPECIALIZATION_CHOICES)
    bio = models.TextField()
    
    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"


class Appointment(models.Model):
    STATUS_CHOICES = (
        ('S', 'Scheduled'),
        ('C', 'Cancelled'),
        ('D', 'Done'),
    )
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='S')
    
    def __str__(self):
        return f"Appointment with Dr. {self.doctor} on {self.date_time}"


class MedicalRecord(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    blood_type = models.CharField(max_length=3)
    medical_history = models.TextField()
    
    def __str__(self):
        return f"Medical Record for {self.patient}"


class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    medication = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255)
    
    def __str__(self):
        return f"Prescription for {self.appointment}"


class Payment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Payment of {self.amount} for {self.appointment}"


class RadiologyTest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=255)
    test_date = models.DateTimeField()
    results = models.TextField()
    
    def __str__(self):
        return f"Radiology Test {self.test_name} for {self.patient}"


class PathologyTest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=255)
    test_date = models.DateTimeField()
    results = models.TextField()
    
    def __str__(self):
        return f"Pathology Test {self.test_name} for {self.patient}"


class Vaccination(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    vaccine_name = models.CharField(max_length=255)
    administered_date = models.DateTimeField()
    
    def __str__(self):
        return f"Vaccination {self.vaccine_name} for {self.patient}"


class MedicalClaim(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    claim_date = models.DateTimeField()
    amount_claimed = models.DecimalField(max_digits=10, decimal_places=2)
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Medical Claim for {self.patient}"


class Consultant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    
    def __str__(self):
        return f"Consultant {self.first_name} {self.last_name}"


class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_billed = models.DateTimeField(default=timezone.now)
    is_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Billing for {self.patient}"


class InventoryItem(models.Model):
    item_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Inventory Item {self.item_name}"


class DoctorInformation(models.Model):
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    qualifications = models.TextField()
    experience = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Information for {self.doctor}"


class DischargeSummary(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    discharge_date = models.DateTimeField()
    summary = models.TextField()
    
    def __str__(self):
        return f"Discharge Summary for {self.patient}"


class PharmacyItem(models.Model):
    item_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Pharmacy Item {self.item_name}"
