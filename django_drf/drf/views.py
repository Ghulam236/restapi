from django.shortcuts import render
from drf.models import Student 
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import requests
#  for class base dviews import decorators
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.
#  for single student 
def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    serilizer_data=StudentSerializer(stu)
    json_data=JSONRenderer().render(serilizer_data.data)
    return HttpResponse(json_data,content_type='application/json')
#  for more than one or all student we use queryset Student.objects.all()
#  we use here many=True in serilizer_data=StudentSerializer(all_stu,many=True)
#  for single data not used but for queryset it is mandatory to use many=True otherwsie error come
def all_student_detail(request):
    all_stu=Student.objects.all()
    serilizer_data=StudentSerializer(all_stu,many=True)
    json_data=JSONRenderer().render(serilizer_data.data)
    return HttpResponse(json_data,content_type='application/json')
@csrf_exempt
def stucreate(request):
    
    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={"msg":"data created"}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
# def stu_crud_api(request):

#  function based crud api 
# @csrf_exempt
# def student_api(request):
#     if request.method =='GET':
#         json_data=request.body
#         print("json_data",json_data)
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         id=python_data.get('id',None)
#         if id is not None:
#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializer(stu)
#             json_data=JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type='application/json')
#         stu=Student.objects.all()
#         serializer=StudentSerializer(stu,many=True)
#         json_data=JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data,content_type='application/json')
#     if request.method=="POST":
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         serializer=StudentSerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res={"msg":"data created"}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(res)
#         return HttpResponse(json_data,content_type='application/json')
    # if request.method=="PUT":
        # json_data=request.body
        # stream=io.BytesIO(json_data)
    #     python_data=JSONParser().parse(stream)
    #     # serializer=StudentSerializer(data=python_data)
    #     id=python_data.get('id')
    #     stu=Student.objects.get(id=id)
    #     print("hiiiiiiiiiiii",stu.name)
    #     print("hiiiiiiiiiiii",stu.id)

    #     serializer=StudentSerializer(stu,data=python_data)
        # if serializer.is_valid():
        #     serializer.save()
#             res={"msg":"data updated"}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')
#     if request.method=="DELETE":
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         # serializer=StudentSerializer(data=python_data)
#         id=python_data.get('id')
#         stu=Student.objects.get(id=id)
#         stu.delete()
#         res={"msg":"data updated"}
#         json_data=JSONRenderer().render(res)
#         return HttpResponse(json_data,content_type='application/json')
#  class based api ##############################
#  also change uls.py
from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(csrf_exempt,name="dispatch")
class StudentAPI(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        print("json_data",type(json_data))
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={"msg":"data created"}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        # serializer=StudentSerializer(data=python_data)
        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        print("hiiiiiiiiiiii",stu.name)
        print("hiiiiiiiiiiii",stu.id)

        serializer=StudentSerializer(stu,data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={"msg":"data updated"}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        # serializer=StudentSerializer(data=python_data)
        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={"msg":"data deleted"}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')


