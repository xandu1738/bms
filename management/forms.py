from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Employee, Position

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username','email', 'password1', 'password2')

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = '__all__'
        
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'