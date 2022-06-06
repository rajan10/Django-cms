from django.contrib import admin
from django.urls import path
from .views import index, create_college,update_college, delete_college


urlpatterns = [
    path('',index, name="index"),
    path('create_college/',create_college, name="create_college"),
    path('update_college/<int:id>', update_college, name="update_college"),
    path('delete_college/<int:id>', delete_college, name="delete_college"),
]