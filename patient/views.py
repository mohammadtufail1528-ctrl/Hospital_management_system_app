
from django.shortcuts import render 
from .models import Patient
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404 , redirect

# Create your views here.
@login_required
def patient_list(request):
    patient=Patient.objects.all()
    return render(request, 'list.html', {'patient':patient})

@login_required
def patient_detail(request, pk):
    patient=get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.name = request.POST.get('name')
        patient.age = request.POST.get('age')
        patient.gender = request.POST.get('gender')
        patient.address = request.POST.get('address')
        patient.phone = request.POST.get('phone')
        patient.blood = request.POST.get('blood')
        
        patient.save()
        return redirect('/patient/')
    return render(request, 'patient_edit.html', {'patient':patient})  

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer

@api_view(['GET'])
def PatientViewSet(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    serializer = PatientSerializer(patient)
    return Response(serializer.data)    


def patient_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        blood = request.POST.get('blood')
        patient = Patient.objects.create(
            name=name,
            age=age,
            gender=gender,
            address=address,
            phone=phone,
            blood=blood
        )
        patient.save()
        return redirect('/patient/')
    return render(request, 'create_new.html')


def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('/patient/')
    return render(request, 'delete.html', {'patient': patient})