from .serializers import PositionSerializer, EmployeeSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from management.models import Position, Employee
from records.models import CashReceipt, InvoiceReceipt, ProformaReceipt, GeneralReceipt

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
# class CashList(ListCreateAPIView):
#     queryset = CashReceipt().objects.all()
#     serializer_class = CashSerializer

# class CashEdit(RetrieveUpdateDestroyAPIView):
#     queryset = CashReceipt().objects.all()
#     serializer_class = CashSerializer
#Invoice CRUD
# class InvoiceList(ListCreateAPIView):
#     queryset = InvoiceReceipt().objects.all()
#     serializer_class = EmployeeSerializer

# class InvoiceEdit(RetrieveUpdateDestroyAPIView):
#     queryset = InvoiceReceipt().objects.all()
#     serializer_class = EmployeeSerializer
#Proforma CRUD
# class ProformaList(ListCreateAPIView):
#     queryset = ProformaReceipt().objects.all()
#     serializer_class = EmployeeSerializer

# class ProformaEdit(RetrieveUpdateDestroyAPIView):
#     queryset = ProformaReceipt().objects.all()
#     serializer_class = EmployeeSerializer
#General CRUD
# class EmployeeList(ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class EmployeeEdit(RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer