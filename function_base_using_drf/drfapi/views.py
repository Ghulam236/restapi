from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from . seriailzers import EmployeeSerializer
# Create your views here.
#  by default it has 'GET'  @api_view(['GET'])
# @api_view()
# def hello_world(request):
#     return Response({"msg":"welldone"})

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def hello_world(request,pk=None):
    if request.method=="GET":
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
      #  return Response({"msg":"This is get"})
      
    if request.method=="POST":
       print(request.data)
       serializer=EmployeeSerializer(data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response({"msg":"data created"})
       return Response(serializer.errors)

       
    #    if i want request data then i shuold 

      #  return Response({"msg":"This is post","data":request.data})
    if request.method=="PUT":
       id=pk
      #  id=request.data.get('id')
       emp=Employee.objects.get(pk=id)
       serializer=EmployeeSerializer(emp,data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response({"msg":"complte data"})
       
       return Response(serializer.errors)
    if request.method=="PATCH":
       id=pk
      #  id=request.data.get('id')
       emp=Employee.objects.get(pk=id)
       serializer=EmployeeSerializer(emp,data=request.data,partial=True)
       if serializer.is_valid():
          serializer.save()
          return Response({"msg":"these field are updated"})
       
       return Response(serializer.errors)
    if request.method=="DELETE":
       id=pk
      #  id=request.data.get('id')
       emp=Employee.objects.get(pk=id)
       emp.delete()
       serializer=EmployeeSerializer(emp,data=request.data)
       return Response({"msg":"these data is deleted"})
    #    print(request.data)
    #    if i want request data then i shuold 

      #  return Response({"msg":"This is putt"})