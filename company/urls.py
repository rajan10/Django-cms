from django.urls import path
from .views import HomeView,CreateCompanyView, UpdateCompanyView, DeleteCompanyView, DetailCompanyView,create_employee

urlpatterns = [
    path('company/', HomeView.as_view(), name="index"),
    path('company/create_company/', CreateCompanyView.as_view(), name="create_company"),
    path('update_company/<int:pk>/', UpdateCompanyView.as_view(), name="update_company"),
    path('detail_company/<int:pk>', DetailCompanyView.as_view(), name="detail_company"),
    path('delete/<int:pk>', DeleteCompanyView.as_view(), name="delete_company"),


    path('company/create_employee/', create_employee, name="create_employee"),

]