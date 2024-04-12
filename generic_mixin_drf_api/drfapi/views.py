from .models import Employee
from .seriailzers import EmployeeSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

class StudentList(GenericAPIView,ListModelMixin):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
class StudentRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
class StudentUpdate(GenericAPIView,UpdateModelMixin):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
class StudentDestroy(GenericAPIView,DestroyModelMixin):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
#  combine create and get all in one class ##################################

class LCStudentList(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
class RUDLCStudentList(GenericAPIView,ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
