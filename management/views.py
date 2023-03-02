from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import EmployeeForm, PositionForm, SignUpForm
from .models import Employee, Position

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('login')
class UserRegistration(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
class UserEditView(UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('dashboard')
    
    def get_object(self):
        return self.request.user

def emps(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employees/emp_list.html', context)
    
def add_emp(request):
    form = EmployeeForm
    emps = Employee.objects.order_by('user')
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form':form, 'emps':emps}
    return render(request, 'employees/add_employee.html', context)

def add_position(request):
    form = PositionForm    
    positions = Position.objects.order_by('position')[:7]

    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form':form, 'positions':positions}
    return render(request, 'employees/new_position.html', context)


