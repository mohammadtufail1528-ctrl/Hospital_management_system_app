from django.shortcuts import get_object_or_404, redirect, render
from .models import Doctor 
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def doctor_list(request):
    doctor=Doctor.objects.all()
    return render(request,'doctor_list.html',{'doctor':doctor})


def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'delete.html', {'doctor': doctor})


def doctor_edit(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.name = request.POST.get('name')
        doctor.age = request.POST.get('age')
        doctor.phone = request.POST.get('phone')
        doctor.specilization = request.POST.get('specilization')
        doctor.save()
        return redirect('doctor_list')
    return render(request, 'doctor_edit.html', {'doctor': doctor})

