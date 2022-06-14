from django.urls import path
from .views import HomeView,CreateCompanyView, UpdateCompanyView, DeleteCompanyView, DetailCompanyView,create_employee, read_employee,update_employee, delete_employee,detail_employee

urlpatterns = [
    path('company/', HomeView.as_view(), name="company_index"),
    path('company/create_company/', CreateCompanyView.as_view(), name="create_company"),
    path('update_company/<int:pk>/', UpdateCompanyView.as_view(), name="update_company"),
    path('detail_company/<int:pk>', DetailCompanyView.as_view(), name="detail_company"),
    path('delete/<int:pk>', DeleteCompanyView.as_view(), name="delete_company"),

    path('company/read_employee/', read_employee, name="read_employee"),
    path('company/create_employee/', create_employee, name="create_employee"),
    path('company/update_employee/<int:id>', update_employee, name="update_employee"),
    path('company/delete/<int:id>', delete_employee, name="delete_employee"),
    path('company/detail_employee/<int:id>',detail_employee, name="detail_employee")


]