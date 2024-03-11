from django.shortcuts import render
from django.http import JsonResponse

from myapplication.models import Employees
from myapplication.serializers import EmployeesSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET','POST'])
def employee_list(request):
   if request.method == 'GET':
    employees = Employees.objects.all()
    serializer = EmployeesSerializer(employees, many=True)
    return JsonResponse({'employees':serializer.data})
   if request.method == 'POST':
     serializer = EmployeesSerializer(data=request.data)
     if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)