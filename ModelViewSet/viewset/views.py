from .models import Employee
from .seriailzers import EmployeeSerializer
from rest_framework import viewsets

class EmployeeModelViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer