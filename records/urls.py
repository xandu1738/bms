from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cash_receipt/', views.add_cash, name='add_cash'),
    path('invoice_receipt/', views.add_invoice, name='add_invoice'),
    path('proforma_receipt/', views.add_proforma, name='add_proforma'),
    path('general_receipt/', views.add_gen, name='gen_receipt'),
    path('employees/', views.add_emp, name='employees'),
    path('position/', views.add_position, name='position'),
]
