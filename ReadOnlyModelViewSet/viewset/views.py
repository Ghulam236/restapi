from .models import Employee
from .seriailzers import EmployeeSerializer
from rest_framework import viewsets

class EmployeeReadOnlyModelViewset(viewsets.ReadOnlyModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer