from myapplication.models import Employees
from rest_framework import serializers

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
