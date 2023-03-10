from django.urls import path
from .views import PositionEdit, PositionList, EmployeeEdit, EmployeeList

urlpatterns = [
    path('', PositionList.as_view(), name='position_list'),
    path('position/<int:pk>/', PositionEdit.as_view(), name='position_ed'),
    path('employees/', EmployeeList.as_view(), name='employee_api'),
    path('employee/<int:pk>', EmployeeEdit.as_view(), name='employee_det'),
]