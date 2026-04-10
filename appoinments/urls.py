from django.urls import path
from .views import appoinment_list, create_appoinment
urlpatterns = [
    path('', appoinment_list, name='appoinment_list'),
    path('create/', create_appoinment, name='create_appoinment'),
]