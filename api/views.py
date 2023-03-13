from .serializers import CashSerializer, GeneralSerializer, InvoiceSerializer, PositionSerializer, EmployeeSerializer, ProformaSerializer, UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from management.models import Position, Employee
from records.models import CashReceipt, InvoiceReceipt, ProformaReceipt, GeneralReceipt
from django.contrib.auth.models import User
class PositionList(ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class PositionEdit(RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

#Employee CRUD
class EmployeeList(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeEdit(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#Cash CRUD
class CashList(ListCreateAPIView):
    queryset = CashReceipt.objects.all()
    serializer_class = CashSerializer

class CashEdit(RetrieveUpdateDestroyAPIView):
    queryset = CashReceipt.objects.all()
    serializer_class = CashSerializer
    
#Invoice CRUD
class InvoiceList(ListCreateAPIView):
    queryset = InvoiceReceipt.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceEdit(RetrieveUpdateDestroyAPIView):
    queryset = InvoiceReceipt.objects.all()
    serializer_class = InvoiceSerializer
    
#Proforma CRUD
class ProformaList(ListCreateAPIView):
    queryset = ProformaReceipt.objects.all()
    serializer_class = ProformaSerializer

class ProformaEdit(RetrieveUpdateDestroyAPIView):
    queryset = ProformaReceipt.objects.all()
    serializer_class = ProformaSerializer

#General CRUD
class GeneralList(ListCreateAPIView):
    queryset = GeneralReceipt.objects.all()
    serializer_class = GeneralSerializer

class GeneralEdit(RetrieveUpdateDestroyAPIView):
    queryset = GeneralReceipt.objects.all()
    serializer_class = GeneralSerializer
    
class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

