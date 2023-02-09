from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .forms import CashReceiptForm, EmployeeForm, PositionForm, InvoiceReceiptForm, GeneralReceiptForm, ProformaReceiptForm

def dashboard(request):
    context = {}
    return render(request, 'records/dashboard.html', context)

def add_cash(request):
    form = CashReceiptForm
    if form.method == 'POST':
        if form.is_valid():
            form.save()
            
    context = {'form':form}
    return render(request, 'records/add_cash.html', context)

def add_gen(request):
    form = GeneralReceiptForm
    context = {'form':form}
    return render(request, 'records/add_cash.html', context)

def add_emp(request):
    form = EmployeeForm
    context = {'form':form}
    return render(request, 'records/add_cash.html', context)

def add_proforma(request):
    form = ProformaReceiptForm
    context = {'form':form}
    return render(request, 'records/add_cash.html', context)

def add_invoice(request):
    form = InvoiceReceiptForm
    context = {'form':form}
    return render(request, 'records/add_cash.html', context)

def add_position(request):
    form = PositionForm
    context = {'form':form}
    return render(request, 'records/add_cash.html', context)
