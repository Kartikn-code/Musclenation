from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.
def  add(request):
    s="the sum of 2+2 is 4!!"
    c=Customer.objects.all()
    a=Customer.objects.using("sqlite3").all()
    return render( request,"home.html",{"data":s,"dbdata":c,"sq":a})


def  about(request):
    s="the sum of 2+2 is 4!!"
    c=Customer.objects.all()
    a=Customer.objects.using("sqlite3").all()
    return render( request,"about.html",{"data":s,"dbdata":c,"sq":a})

def display(request,user_id):
    user_id=get_object_or_404(Customer,id=user_id) #pk=primary key
    cdata=Customer.objects.all()
    context={
        'user_id':user_id, 
        'data':cdata
    }
    return render (request,"display.html",{
        'user_id':user_id, 
        'data':cdata
    })

