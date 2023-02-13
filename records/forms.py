from django import forms
from .models import GeneralReceipt, CashReceipt, InvoiceReceipt, ProformaReceipt, Position, Employee

class GeneralReceiptForm(forms.ModelForm):
    class Meta:
        model = GeneralReceipt
        fields = ['name','amount','reason','issued_by','received_by']
        
class CashReceiptForm(forms.ModelForm):
    class Meta:
        model = CashReceipt
        fields = ['sale_type','quantity','unit', 'item', 'price']
        
class InvoiceReceiptForm(forms.ModelForm):
    class Meta:
        model = InvoiceReceipt
        fields = ['quantity','unit','item','price','issued_by','received_by']
        
class ProformaReceiptForm(forms.ModelForm):
    class Meta:
        model = ProformaReceipt
        fields = ['quantity','unit','item','price']
        
class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = '__all__'
        
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'