from django.shortcuts import render,redirect, get_object_or_404
from django.views import generic
from company.models import Company, Employee
from django.views.generic import View
from .forms import CompanyForm, EmployeeForm
from django.urls import reverse
# Create your views here.

#class base views implementation of Company
class HomeView(generic.ListView):
    template_name='company/index.html'
    model=Company

class CreateCompanyView(View):
    def get(self,request):
        context={}
        form=CompanyForm()
        context['form']=form
        return render(request,template_name='company/create_company.html',context=context)
    def post(self,request):
        form=CompanyForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            company_type = form.cleaned_data['company_type']
            vat_id_number = form.cleaned_data['vat_id_number']
            company=Company(company_name=company_name, company_type=company_type, vat_id_number=vat_id_number)
            company.save()
            return redirect('/company/')

class UpdateCompanyView(View):
    def get(self,request,pk):
        # print(pk)
        # return redirect("/")
        context={}
        company=Company.objects.get(id=pk)
        data={'company_name':company.company_name,'company_type':company.company_type,'vat_id_number':company.vat_id_number}
        form=CompanyForm(data)
        context['form']=form
        return render(request, template_name='college/update_company.html',context=context)
    def post(self,request,pk):
        company=Company.objects.get(id=pk)
        form=CompanyForm(request.POST)
        if form.is_valid():
            company.company_name=form.cleaned_data['company_name']
            company.company_type=form.cleaned_data['company_type']
            company.vat_id_number = form.cleaned_data['vat_id_number']

            company.save(update_fields=['company_name', 'company_type', 'vat_id_number'])
            return redirect('/company/')

class DetailCompanyView(generic.DetailView):
    model=Company
    template_name = 'company/detail_company.html'

class DeleteCompanyView(generic.DeleteView):
    model=Company
    template_name = 'company/delete_company.html'
    # all generic. Views have below function
    success_url='/company'
        #for url use /

# Function-base views implementation
# company/create_employee/'
def create_employee(request):
    if request.method=="GET":
        context={}
        form =EmployeeForm()
        context['form']=form
        return render(request,template_name="employee/create_employee.html", context=context)
    if request.method=="POST":
        form=EmployeeForm(request.POST)

        if form.is_valid():
            #both ways possible
            # company = form.cleaned_data['company']
            company = Company.objects.all()[0]

            full_name= form.cleaned_data['full_name']
            designation=form.cleaned_data['designation']
            email= form.cleaned_data['email']
            phone= form.cleaned_data['phone']

            employee=Employee(company=company, full_name=full_name,designation=designation,email=email,phone=phone)
            employee.save()
            # 2 url
            return redirect('/company/read_employee')

def read_employee(request):
    employees=Employee.objects.all()

    return render(request, "employee/read_employee.html",{'employees':employees})

def update_employee(request, id):
    employee=get_object_or_404(Employee, pk=id)
    if request.method=="GET":
        data={'full_name':employee.full_name, 'designation':employee.designation,'email':employee.email, 'phone':employee.phone}
        form=EmployeeForm(data)
        context={}
        context['form']=form
        return render(request, template_name='employee/update_employee.html', context=context)
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            employee.full_name=form.cleaned_data['full_name']
            employee.designation=form.cleaned_data['designation']
            employee.email=form.cleaned_data['email']
            employee.phone=form.cleaned_data['phone']
            employee.save(update_fields=['full_name','designation','email','phone'])
            return redirect('/company/read_employee')

def detail_employee(request,id):
    employee=Employee.objects.filter(pk=id)
    context={}
    context['data'] = {'full_name': employee.full_name, 'designation': employee.designation, 'email': employee.email,
            'phone': employee.phone}
    return render(request,template_name='employee/detail_employee.html',context=context)

def delete_employee(request,id):
    employee=Employee.objects.filter(pk=id)
    employee.delete()
    return redirect('/company/read_employee')





