from django.urls import path

from.views import desboard

urlpatterns = [
    path('', desboard)
    
]
