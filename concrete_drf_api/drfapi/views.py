from .models import Employee
from .seriailzers import EmployeeSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,ListCreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView

class StudentList(ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

    
class StudentCreate(CreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
   
class StudentRetrieve(RetrieveAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
   
class StudentUpdate(UpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    
class StudentDestroy(DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
   
#  combine create and get all in one class ##################################

class LCStudentList(ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    
class RUDLCStudentList(RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
