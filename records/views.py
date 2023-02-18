from django.shortcuts import render
from django.db.models import Sum, F
from django.views.generic import TemplateView, DetailView, ListView 
from .models import *
from .forms import CashReceiptForm, InvoiceReceiptForm, GeneralReceiptForm, ProformaReceiptForm
from .exportto import sales_to_pdf, sales_to_txt
class CashChartView(TemplateView):
    model = CashReceipt
    template_name = 'records/cash_charts.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = CashReceipt.objects.all()
        return context

def receipt_menu(request):
    return render('records/receipts/receipt_menu.html')
  
def receipts(request):
    return render(request, 'records/receipts/receipts_menu.html')

class General(DetailView):
    model = GeneralReceipt
    template_name = 'records/receipts/general_receipt.html'

def dashboard(request):
    context = {}
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
    cash = CashReceipt.objects.all()
    # labels = []
    # data = []
    # queryset = CashReceipt.objects.all()
    
    # for sale in queryset:
    #     labels.append(sale.item)
    #     data.append(sale.price)
    # context = {'labels':labels, 'data':data}
    context = {'cash':cash}
    return render(request, 'records/cash_charts.html', context)

def sales_txt(request):
    return sales_to_txt(CashReceipt)

def sales_pdf(request):
    return sales_to_pdf(CashReceipt)