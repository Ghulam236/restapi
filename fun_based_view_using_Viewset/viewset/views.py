from .models import Employee
from .seriailzers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


class StudenViewtList(viewsets.ViewSet):
    def list(self,request):
      emp=Employee.objects.all()
    
      serializer_class=EmployeeSerializer(emp,many=True)
      return Response(serializer_class.data)

    
    def retrieve(self,request,pk=None):
      id=pk
      if id is not None:
        emp=Employee.objects.get(id=id)
        serializer_class=EmployeeSerializer(emp)
        return Response(serializer_class.data)
    def create(self,request):
       serializer=EmployeeSerializer(data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
       return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
          
      
      
    def update(self,request,pk):
        id=pk
        if id is not None:
            emp=Employee.objects.get(id=pk)
            serializer_class=EmployeeSerializer(emp,request.data)
            if serializer_class.is_valid():
               serializer_class.save()
               return Response({'msg':'data updated'})
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
      
          
    def partial_update(self,request,pk):
        id=pk
        if id is not None:
            emp=Employee.objects.get(pk=id)
            serializer_class=EmployeeSerializer(emp,data=request.data,partial=True)
            if serializer_class.is_valid():
               serializer_class.save()
               return Response({'msg':'partial data updated'})
            return Response(serializer_class.errors)
    def destroy(self,request,pk):
        id=pk
       
        emp=Employee.objects.get(pk=id)
        emp.delete()
            
        return Response({'msg':'partial data updated'})
            
   