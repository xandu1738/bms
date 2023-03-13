from django.urls import path
from .views import PositionEdit, PositionList, EmployeeEdit, EmployeeList, CashList, CashEdit, UserList
from .views import InvoiceList, InvoiceEdit, ProformaList, ProformaEdit, GeneralList, GeneralEdit

urlpatterns = [
    path('', PositionList.as_view(), name='position_list'),
    path('position/<int:pk>/', PositionEdit.as_view(), name='position_ed'),
    path('employees/', EmployeeList.as_view(), name='employee_api'),
    path('employee/<int:pk>', EmployeeEdit.as_view(), name='employee_det'),
    path('cash_api/', CashList.as_view(), name='cash_api'),
    path('cash_api/<int:pk>', CashEdit.as_view(), name='cash_det'),
    path('invoice_api/', InvoiceList.as_view(), name='invoice_api'),
    path('invoice_api/<int:pk>', InvoiceEdit.as_view(), name='invoice_det'),
    path('proforma_api/', ProformaList.as_view(), name='proforma_api'),
    path('proforma_api/<int:pk>', ProformaEdit.as_view(), name='proforma_det'),
    path('general_api/', GeneralList.as_view(), name='general_api'),
    path('general_api/<int:pk>', GeneralEdit.as_view(), name='general_det'),
    path('user_api/', UserList.as_view(), name='user_api'),
]