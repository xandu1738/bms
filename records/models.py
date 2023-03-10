from django.db import models
from django.urls import reverse

from management.models import Employee, Position

SALE_TYPE = (('Debit', 'Debit'), ('Credit', 'Credit'))

UNIT_OF_QUANTITY = (('Pieces', 'Pieces'), ('Meters', 'Meters'),('Boxes','Boxes'),('Cartons','Cartons'))

class InvoiceReceipt(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=100, choices=UNIT_OF_QUANTITY, default='Pieces')
    item = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.FloatField(default=0)

    issued_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    received_by = models.CharField(max_length=255)
    
    def __str__(self):
        return self.received_by + " " + str(self.quantity)
    
    def save(self, *args, **kwargs):
        self.total = self.quantity * self.price
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("add_invoice")
    
class ProformaReceipt(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=100, choices=UNIT_OF_QUANTITY, default='Pieces')
    item = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.FloatField(default=0)
    
    def __str__(self):
        return self.item + " " + str(self.quantity)
    
    def save(self, *args, **kwargs):
        self.total = self.quantity * self.price
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("add_proforma")
    
class CashReceipt(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    sale_type = models.CharField(max_length=8, choices=SALE_TYPE, default='Deb')
    quantity = models.IntegerField()
    unit = models.CharField(max_length=100, choices=UNIT_OF_QUANTITY, default='Pieces')
    item = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.FloatField(default=0)
    
    def __str__(self):
        return self.item + " " + str(self.quantity)
    
    def save(self, *args, **kwargs):
        self.total = self.quantity * self.price
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("add_cash")
    
class GeneralReceipt(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.CharField(max_length=255)
    issued_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    received_by = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name + " " + str(self.amount)
    
    def get_absolute_url(self):
        return reverse("gen_receipt")
    
