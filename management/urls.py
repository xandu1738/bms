from django.urls import path
from .views import UserRegistration
from . import views

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('add_employees/', views.add_emp, name='add_employees'),
    path('position/', views.add_position, name='position'),
    path('employees/', views.emps, name='employees'),
]

