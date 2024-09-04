from django import forms
from .models import *
class CustomerForm(forms.ModelForm):
    class Meta:
        model=CustomerDetails
        fields='__all__'


