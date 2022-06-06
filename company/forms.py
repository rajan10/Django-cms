from django import forms
from .models import  Company,Employee


class CompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields =['company_name','company_type' ,'vat_id_number']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['full_name','designation','email','phone']
