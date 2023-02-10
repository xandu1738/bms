from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

SALE_TYPE = (('Deb', 'Debit'), ('Cre', 'Credit'))

class Position(models.Model):
    position = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.position
    
    def get_absolute_url(self):
        return reverse("position")
    

class Employee(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    #profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    
    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse("employees")

class InvoiceReceipt(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    item = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    issued_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    received_by = models.CharField(max_length=255)
    
    def __str__(self):
        return self.received_by + " " + str(self.quantity)
    
    def get_absolute_url(self):
        return reverse("add_invoice")
    
class ProformaReceipt(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    item = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.item + " " + str(self.quantity)
    
    def get_absolute_url(self):
        return reverse("add_proforma")
    
class CashReceipt(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    sale_type = models.CharField(max_length=8, choices=SALE_TYPE, default='Deb')
    quantity = models.IntegerField()
    item = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.item + " " + str(self.quantity)
    
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
    
