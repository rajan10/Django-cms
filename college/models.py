from django.db import models
from django import forms
# Create your models here.
class College(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)

    def __str__(self):
        return self.name