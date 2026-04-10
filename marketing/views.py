from django.shortcuts import render

# Create your views here.
def home(request):
    
    return render(request,'marketing_home.html')

def contact(request):
    return render(request,'marketing_contact.html')
def emergency(request):
    return render(request,'emergency.html')
def patient_support(request):
    return render(request,'patient_support.html')