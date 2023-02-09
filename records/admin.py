from django.contrib import admin
from .models import Position, ProformaReceipt, InvoiceReceipt, CashReceipt, GeneralReceipt, Employee

admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(CashReceipt)
admin.site.register(InvoiceReceipt)
admin.site.register(ProformaReceipt)
admin.site.register(GeneralReceipt)
