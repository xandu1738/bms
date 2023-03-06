from django.shortcuts import render, redirect
from django.db.models import Sum, F
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.views.generic import TemplateView, DetailView, ListView 
from .models import *
from .forms import CashReceiptForm, ContactForm, InvoiceReceiptForm, GeneralReceiptForm, ProformaReceiptForm
from .exportto import sales_to_pdf, sales_to_txt
from management.models import Employee
from datetime import datetime
from django.template.defaultfilters import floatformat
from django.contrib import messages
from io import BytesIO
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

import numpy as np
class CashChartView(TemplateView):
    model = CashReceipt
    template_name = 'records/receipts/cash_charts.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = CashReceipt.objects.all()
        return context
  
def receipts(request):
    return render(request, 'records/receipts/receipts_menu.html')

class General(DetailView):
    model = GeneralReceipt
    template_name = 'records/receipts/general_receipt.html'

def dashboard(request):
    
    day = datetime.today()
    
    current_month = datetime.now().month
    current_year = datetime.now().year
    
    this_month = np.array(CashReceipt.objects.filter(date__month=current_month, date__year=current_year).values_list('total', flat=True))
    ns = np.sum(this_month)
    np_sum = floatformat(ns, 2)
    
    curr_month = CashReceipt.objects.filter(date__month=current_month, date__year=current_year)
    
    specific_month = 2  # February
    specific_year = 2023
    
    spec_month = CashReceipt.objects.filter(date__month=specific_month, date__year=specific_year)
    
    day_bal = np.array(CashReceipt.objects.filter(date__year=day.year, date__month=day.month, date__day=day.day).values_list('total', flat=True))
    tb = np.sum(day_bal)
    today_bal = floatformat(tb, 2)
    
    cash = CashReceipt.objects.all()
    employees = Employee.objects.all()
    context = {'cash': cash, 'np_sum':np_sum,'today_bal':today_bal , 'employees': employees,'curr_month': curr_month, 'spec_month': spec_month}
    return render(request, 'records/dashboard.html', context)

def add_cash(request):
    sales = CashReceipt.objects.order_by('-date')[:5]
    form = CashReceiptForm()
    debit = CashReceipt.objects.filter(sale_type="Debit").aggregate(Sum('total'))['total__sum']    
    credit = CashReceipt.objects.filter(sale_type="Credit").aggregate(Sum('total'))['total__sum']

    if request.method == 'POST':
        form = CashReceiptForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, ('Cash Receipt added successfully'))
            
            
    context = {'form':form, 'sales':sales, 'debit':debit, 'credit':credit}
    return render(request, 'records/receipts/add_cash.html', context)

def add_gen(request):
    sales = GeneralReceipt.objects.order_by('-date')[:7]
    form = GeneralReceiptForm
    if request.method == 'POST':
        form = GeneralReceiptForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, ('General Receipt added successfully'))
            
    context = {'form':form, 'sales':sales}
    return render(request, 'records/receipts/add_genreceipt.html', context)

def add_proforma(request):
    form = ProformaReceiptForm
    prdts = ProformaReceipt.objects.order_by('-date')[:7]
    
    if request.method == 'POST':
        form = ProformaReceiptForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, ('Proforma added successfully'))
            
    context = {'form':form, 'prdts':prdts}
    return render(request, 'records/receipts/add_proforma.html', context)

def add_invoice(request):
    form = InvoiceReceiptForm
    prdts = InvoiceReceipt.objects.order_by('-date')[:7]
    if request.method == 'POST':
        form = InvoiceReceiptForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, ('Invoice added successfully'))
            
    context = {'form':form, 'prdts':prdts}
    return render(request, 'records/receipts/add_invoice.html', context)

def cash_stats(request):
    labels = []
    data = []
    queryset = CashReceipt.objects.all()
    
    for sale in queryset:
        labels.append(sale.item)
        data.append(sale.price)
    context = {'labels':labels, 'data':data}
    return render(request, 'records/cash_charts.html', context)

def sales_txt(request):
    return sales_to_txt(CashReceipt)

def sales_pdf(request):
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    
    textOb = c.beginText()
    textOb.setTextOrigin(inch, inch)
    textOb.setFont("Helvetica", 12)
    
    sales = CashReceipt.objects.all()
    
    lines = []
    
    for sale in sales:
        lines.append(sale.date)
        lines.append(sale.sale_type)
        lines.append(sale.quantity)
        lines.append(sale.unit)
        lines.append(sale.item)
        lines.append(sale.price)
        lines.append(sale.total)
        lines.append(" ")
    
    for line in lines:
        textOb.textLine(line)
    
    c.drawText(textOb)
    c.showPage()
    c.save()
    buf.seek(0)
    
    return FileResponse(buf, as_attachment=True, filename='sales.pdf')

def templatedef(request):
    return render(request, 'default.html')

def welcome(request):
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            em_context = {'name':name, 'email':email, 'message':message}
            html = render_to_string('email_template.html', em_context)
            
            send_mail(
                'Customer Contact Form',
                f'Name: {name}\nEmail: {email}\nMessage {message}\n',
                settings.DEFAULT_FROM_EMAIL,
                ['settings.EMAIL_HOST_USER'],
                html_message=html,
                fail_silently=False,
            )
            messages.success(request,('Email Submitted'))
            return redirect('welcome')
            
    context = {'form':form}
    return render(request, 'welcome.html', context)
