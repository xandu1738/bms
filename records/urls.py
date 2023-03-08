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
    
    path('cash_update/<int:pk>/', views.cash_update, name="cash_update"),
    path('invoice_update/<int:pk>/', views.invoice_update, name="invoice_update"),
    path('proforma_update/<int:pk>/', views.proforma_update, name="proforma_update"),
    path('gr_update/<int:pk>/', views.gr_update, name="gr_update"),
    
    path('delete_sale/<int:pk>/', views.delete_cash, name="del_cash"),
    path('delete_invoice/<int:pk>/', views.delete_invoice, name="del_invoice"),
    path('delete_proforma/<int:pk>/', views.delete_proforma, name="del_proforma"),
    path('delete_gr/<int:pk>/', views.delete_gr, name="del_gr"),
    
    path('sendit', views.welcome, name="send"),
]

