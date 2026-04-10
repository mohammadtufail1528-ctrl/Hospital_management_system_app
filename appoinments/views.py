from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Appoinment 
from doctor.models import Doctor 
from patient.models import Patient
from django.shortcuts import get_object_or_404
# Create your views here.

def appoinment_list(request):
    appoinments = Appoinment.objects.all()
    return render(request, 'app_list.html', {'appoinments': appoinments})


def create_appoinment(request):
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    if request.method == 'POST':
        patient_id = request.POST.get('patient')
        doctor_id = request.POST.get('doctor_id')
        date = request.POST.get('date')
        time = request.POST.get('time')
        reason = request.POST.get('reason')

        patient = get_object_or_404(Patient, id=patient_id)
        doctor = get_object_or_404(Doctor, id=doctor_id)

        Appoinment.objects.create(patient=patient, doctor=doctor, date=date, time=time, reason=reason)
        return redirect('appoinment_list')

    return render(request, 'create_appoinment.html', {'doctors': doctors, 'patients': patients})