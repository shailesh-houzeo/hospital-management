from django.contrib.auth.decorators import user_passes_test

def patient_required(view_func):
    decorated_view_func = user_passes_test(lambda u: u.is_patient, login_url='login')(view_func)
    return decorated_view_func

def doctor_required(view_func):
    decorated_view_func = user_passes_test(lambda u: u.is_doctor, login_url='login')(view_func)
    return decorated_view_func
