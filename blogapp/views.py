from django.shortcuts import render
from .models import *
# Create your views here.
def a1(request):
    a=Gymblog.objects.all()
    return render( request,"blog.html",{"dbdata":a})