from django import forms
from . import models


class CollegeForm(forms.Form):
    name = forms.CharField(required=True)
    address = forms.CharField(required=True)
    phone = forms.CharField()
