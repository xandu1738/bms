from django.contrib import admin
from .models import ProformaReceipt, InvoiceReceipt, CashReceipt, GeneralReceipt

admin.site.register(CashReceipt)
admin.site.register(InvoiceReceipt)
admin.site.register(ProformaReceipt)
admin.site.register(GeneralReceipt)
