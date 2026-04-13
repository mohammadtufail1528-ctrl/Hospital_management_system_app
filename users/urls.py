from django.urls import path

from doctor import views
from .views import signup, user_login
  
urlpatterns = [
      path('signup/', signup),
      path('login/', user_login),

  ]