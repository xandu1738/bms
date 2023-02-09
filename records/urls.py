from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cash_receipt/', views.add_cash, name='add_cash'),
    path('invoice_receipt/', views.add_invoice, name='add_cash'),
    path('proforma_receipt/', views.add_proforma, name='add_cash'),
    path('general_receipt/', views.add_gen, name='add_cash'),
    path('employees/', views.add_emp, name='add_cash'),
    path('position/', views.add_position, name='add_cash'),
]
