from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=10)
    department = models.CharField(max_length=10)
    salary = models.IntegerField()
    def __str__(self):
        return self.name
