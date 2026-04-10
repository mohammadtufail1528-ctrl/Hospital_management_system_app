from django.urls import path

from .views import home,contact , emergency, patient_support

urlpatterns = [
    path('', home),
    path('contact/', contact),
    path('emergency/', emergency),
    path('support/', patient_support),
    
]
    
    

