from django import forms
from .models import *
class CustomerForm(forms.ModelForm):
    class Meta:
        model=CustomerDetails
        fields='__all__'


class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['file']


