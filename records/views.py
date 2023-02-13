from django.shortcuts import render
from django.db.models import Sum, F
from django.views.generic import TemplateView
from .models import *
from .forms import CashReceiptForm, EmployeeForm, PositionForm, InvoiceReceiptForm, GeneralReceiptForm, ProformaReceiptForm, PositionForm

class CashChartView(TemplateView):
    template_name = 'records/cash_charts.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = CashReceipt.objects.all()
        return context

def dashboard(request):
    context = {}
    return render(request, 'records/dashboard.html', context)

def add_cash(request):
    
    sales = CashReceipt.objects.order_by('-date')[:5]
    
    form = CashReceiptForm()
    
    debit = CashReceipt.objects.filter(sale_type="Debit").aggregate(Sum('total'))['total__sum']
    
    credit = CashReceipt.objects.filter(sale_type="Credit").aggregate(Sum('total'))['total__sum']
  
    # for d in debit:
    #     total_d = d.price * d.quantity
      
    if request.method == 'POST':
        form = CashReceiptForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form':form, 'sales':sales, 'debit':debit, 'credit':credit}
    return render(request, 'records/add_cash.html', context)

def add_gen(request):
    sales = GeneralReceipt.objects.order_by('-date')[:7]
    form = GeneralReceiptForm
    if request.method == 'POST':
        form = GeneralReceiptForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form':form, 'sales':sales}
    return render(request, 'records/add_genreceipt.html', context)

def add_emp(request):
    
    form = EmployeeForm
    emps = Employee.objects.order_by('user')[:7]
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form':form, 'emps':emps}
    return render(request, 'records/add_employee.html', context)

def add_proforma(request):
    form = ProformaReceiptForm
    
    prdts = ProformaReceipt.objects.order_by('-date')[:7]
    
    if request.method == 'POST':
        form = ProformaReceiptForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form, 'prdts':prdts}
    return render(request, 'records/add_proforma.html', context)

def add_invoice(request):
    form = InvoiceReceiptForm
    prdts = InvoiceReceipt.objects.order_by('-date')[:7]
    if request.method == 'POST':
        form = InvoiceReceiptForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form, 'prdts':prdts}
    return render(request, 'records/add_invoice.html', context)

def add_position(request):
    
    form = PositionForm
    
    positions = Position.objects.order_by('position')[:7]
    
    if request.method == 'POST':
        
        form = PositionForm(request.POST)
        
        if form.is_valid():
            form.save()
    
    context = {'form':form, 'positions':positions}
    return render(request, 'records/new_position.html', context)

def cash_stats(request):
    
    labels = []
    
    data = []
    
    queryset = CashReceipt.objects.all()
    
    for sale in queryset:
        labels.append(sale.item)
        
        data.append(sale.price)
        
        # res = CashReceipt.objects.aggregate(Sum('price'))
   
    
    context = {'labels':labels, 'data':data}
    
    return render(request, 'records/cash_charts.html', context)
