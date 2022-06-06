from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    company_name=models.CharField(max_length=150)
    company_type=models.CharField(max_length=150)
    vat_id_number=models.CharField(max_length=10)

    def __str__(self):
        return self.company_name
class Employee(models.Model):
    company=models.ForeignKey(Company, on_delete=models.CASCADE, related_name='companies')
    full_name=models.CharField(max_length=100)
    designation=models.CharField(max_length=150)
    email=models.EmailField()
    phone=models.CharField(max_length=10)

    def __str__(self):
        return self.full_name
