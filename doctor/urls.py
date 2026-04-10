from django.urls import path

from.views import doctor_delete, doctor_edit, doctor_list

urlpatterns = [
   path('', doctor_list, name='doctor_list'),
    path('<int:pk>/edit/', doctor_edit, name='doctor_edit'),
    path('<int:pk>/delete/', doctor_delete, name='doctor_delete'),
    
]
