from rest_framework import serializers
from records.models import CashReceipt, ProformaReceipt, InvoiceReceipt, GeneralReceipt
from management.models import Position, Employee

class CashSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashReceipt
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceReceipt
        fields = '__all__'
class ProformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProformaReceipt
        fields = '__all__'

class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralReceipt
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'