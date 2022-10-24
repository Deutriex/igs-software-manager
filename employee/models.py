from django.db import models
from django.urls import reverse
from department.models import Department
from rest_framework import serializers

# Create your models here.
class Employee(models.Model):
    name        = models.CharField(max_length=1000)
    email       = models.EmailField(max_length=254) 
    department  = models.ForeignKey(Department, related_name = 'department_name', on_delete=models.CASCADE)

    def get_department_name(self):
        return self.department.name