from django.urls import path
from . import views
from .views import General

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('sales_to_txt', views.sales_txt, name='sales_to_txt'),
    path('sales_to_pdf', views.sales_pdf, name='sales_to_pdf'),    
    path('cash_receipt/', views.add_cash, name='add_cash'),
    path('invoice_receipt/', views.add_invoice, name='add_invoice'),
    path('proforma_receipt/', views.add_proforma, name='add_proforma'),
    path('general_receipt/', views.add_gen, name='gen_receipt'),
    path('general_receipt/<int:pk>', General.as_view(), name='gen_receipt'),
    path('cash_stats/', views.cash_stats, name='cash_stats'),
    path('cash_detail/<int:pk>/', views.cash_detail, name="cash_detail"),
    path('sendit', views.welcome, name="send"),
]

