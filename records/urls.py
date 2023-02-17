from django.urls import path
from . import views
from .views import CashChartView, General

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('sales_to_txt', views.sales_txt, name='sales_to_txt'),
    path('sales_to_pdf', views.sales_pdf, name='sales_to_pdf'),    
    path('cash_receipt/', views.add_cash, name='add_cash'),
    path('invoice_receipt/', views.add_invoice, name='add_invoice'),
    path('proforma_receipt/', views.add_proforma, name='add_proforma'),
    path('general_receipt/', views.add_gen, name='gen_receipt'),
    path('general_receipt/<int:pk>', General.as_view(), name='gen_receipt'),
    path('employees/', views.add_emp, name='employees'),
    path('position/', views.add_position, name='position'),
    path('cash_stats/', CashChartView.as_view(), name='cash_stats'),
    path('receipts/', views.receipts, name='receipts'),
]

