from django.urls import path

from.views import PatientViewSet, delete_patient, patient_list, patient_detail
from .views import patient_create
urlpatterns = [
    path('', patient_list),
    path('<int:pk>/edit/', patient_detail),
    path('<int:pk>/delete/', delete_patient),
    path('create/', patient_create),
    path('api/patients/<int:pk>/', PatientViewSet),
]