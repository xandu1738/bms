from django.urls import path
from .views import UserRegistration, UserEditView, PasswordsChangeView
from . import views

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='profile_edit'),
    path('add_employees/', views.add_emp, name='add_employees'),
    path('position/', views.add_position, name='position'),
    path('employees/', views.emps, name='employees'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html'), name='password'),
]

