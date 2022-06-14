from django.shortcuts import render,redirect, get_object_or_404
from .forms import CollegeForm
from college.models import College

# function base views
# Create your views here.
def index(request):
    colleges=College.objects.all()
    return render(request,'college/index.html', {'colleges':colleges})

def create_college(request):
    if request.method=='GET':
        context = {}
        form=CollegeForm()
        context['form']=form
        return render(request, template_name='college/create_college.html',context=context)
    if request.method=='POST':
        form=CollegeForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            college=College(name=name,address=address, phone=phone)
            college.save()
            return redirect('college/index')

def update_college(request, id):
    college=get_object_or_404(College, pk=id)
    if request.method=='GET':
        data={'name':college.name,'address':college.address,'phone':college.phone}
        form=CollegeForm(data)
        context={}
        context['form']=form
        return render(request,template_name='college/college_update.html', context=context)
    if request.method=='POST':
        form=CollegeForm(request.POST)
        if form.is_valid():
            college.name=form.cleaned_data['name']
            college.address = form.cleaned_data['address']
            college.phone = form.cleaned_data['phone']
            college.save(update_fields=['name','address','phone'])
            return redirect('index')

def delete_college(request, id):
    college=College.objects.get(pk=id)
    college.delete()
    return redirect('index')
