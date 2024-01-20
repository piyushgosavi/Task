from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

class StudentAPIView(APIView):
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id) 
            serializers = StudentSerializers(stu)
            return Response(serializers.data)
        stu = Student.objects.all()
        serializers = StudentSerializers(stu,many=True)
        return Response(serializers.data)
    
    def post(self,request,format=None):
        serializers = StudentSerializers(data=request.data)
        if serializers.is_valid():
           serializers.save()
           return Response({'msg':'Data is Created'},status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk,format=None):
        id = pk
        stu = Student.objects.get(id=id)
        serializers = StudentSerializers(stu,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data is Deleted'})
       

    
class SectionAPIView(APIView):
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            stu = Section.objects.get(id=id) 
            serializers = SectionSerializers(stu)
            return Response(serializers.data)
        stu = Section.objects.all()
        serializers = SectionSerializers(stu,many=True)
        return Response(serializers.data)
    
    def post(self,request,format=None):
        serializers = SectionSerializers(data=request.data)
        if serializers.is_valid():
           serializers.save()
           return Response({'msg':'Data is Created'},status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk,format=None):
        id = pk
        stu = Section.objects.get(id=id)
        serializers = SectionSerializers(stu,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        id = pk
        stu = Section.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data is Deleted'})
       
