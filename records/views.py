from django.shortcuts import render
from django.db.models import Sum, F
from django.views.generic import TemplateView, DetailView, ListView 
from .models import *
from .forms import CashReceiptForm, InvoiceReceiptForm, GeneralReceiptForm, ProformaReceiptForm
from .exportto import sales_to_pdf, sales_to_txt
from management.models import Employee

from io import BytesIO
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
class CashChartView(TemplateView):
    model = CashReceipt
    template_name = 'records/receipts/cash_charts.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = CashReceipt.objects.all()
        return context

def receipt_menu(request):
    return render(request, 'records/receipts/receipt_menu.html')
  
def receipts(request):
    return render(request, 'records/receipts/receipts_menu.html')

class General(DetailView):
    model = GeneralReceipt
    template_name = 'records/receipts/general_receipt.html'

def dashboard(request):
    cash = CashReceipt.objects.all()
    employees = Employee.objects.all()
    context = {'cash': cash, 'employees': employees}
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
            
    context = {'form':form, 'sales':sales, 'debit':debit, 'credit':credit}
    return render(request, 'records/receipts/add_cash.html', context)

def add_gen(request):
    sales = GeneralReceipt.objects.order_by('-date')[:7]
    form = GeneralReceiptForm
    if request.method == 'POST':
        form = GeneralReceiptForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form':form, 'sales':sales}
    return render(request, 'records/receipts/add_genreceipt.html', context)

def add_proforma(request):
    form = ProformaReceiptForm
    prdts = ProformaReceipt.objects.order_by('-date')[:7]
    
    if request.method == 'POST':
        form = ProformaReceiptForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form':form, 'prdts':prdts}
    return render(request, 'records/receipts/add_proforma.html', context)

def add_invoice(request):
    form = InvoiceReceiptForm
    prdts = InvoiceReceipt.objects.order_by('-date')[:7]
    if request.method == 'POST':
        form = InvoiceReceiptForm(request.POST)
        if form.is_valid():
            form.save()
            
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
    return render(request, 'welcome.html')