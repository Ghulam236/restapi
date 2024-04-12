from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.views import APIView
# Create your views here.
#  by default it has 'GET'  @api_view(['GET'])
# @api_view()
# def hello_world(request):
#     return Response({"msg":"welldone"})
class StudentAPI(APIView):
   def get(self,request,pk=None,format=None):
      id=pk
      # id=request.data.get('id')
      if id is not None:
         emp=Employee.objects.get(pk=id)
         serializer=EmployeeSerializer(emp)
      # if serializer.is_valid():
      #  serializer.save()
       

    #    print(request.data)
    #    if i want request data then i shuold 

         return Response(serializer.data)
      emp=Employee.objects.all()
      serializer=EmployeeSerializer(emp,many=True)
      return Response(serializer.data)
      

   def post(self,request,format=None):
    serializer=EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"msg":"data created"})
    return Response(serializer.errors)
   def put(self,request,pk=None,format=None):
       id=pk
      #  id=request.data.get('id')
       emp=Employee.objects.get(pk=id)
       serializer=EmployeeSerializer(emp,data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response({"msg":"complte data"})
       
       return Response(serializer.errors)
   def patch(self,request,format=None,pk=None):
       id=pk
      #  id=request.data.get('id')
       emp=Employee.objects.get(pk=id)
       serializer=EmployeeSerializer(emp,data=request.data,partial=True)
       if serializer.is_valid():
          serializer.save()
          return Response({"msg":"these field are updated"})
       
       return Response(serializer.errors)
   def delete(self,request,format=None,pk=None):
       id=pk
      #  id=request.data.get('id')
       emp=Employee.objects.get(pk=id)
       emp.delete()
      
       return Response({"msg":"these data is deleted"})

    



    
      
  
       

       
    
       
   
