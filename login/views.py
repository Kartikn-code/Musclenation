from django.shortcuts import render,redirect,get_object_or_404
from .models import*
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.contrib import messages

# Create your views here.
def login_custom(request):
     return render(request,"login.html",)
def loginpage(request):
     return render(request,"loginpage.html",)
def Products(request):
     user=request.session.get('username')
     return render(request,"PRODUCTS.html",{'logged_user':user})
def login_cred(request):
     return render (request,"login_cred.html",)
def registeration(request):
     print(request.POST)
     if request.method=="POST":
          username=request.POST["username"]
          password=request.POST["password"]
          user=User.objects.create_user(username=username,email=None,password=password)
          user.save()
          return redirect("login_cred")
     return render(request,"login_cred.html")
def userlogin(request):
     username=request.POST["username"]
     password=request.POST["password"]
     user=authenticate(username=username,email=None,password=password)
     if user is not None:
          login(request, user)
          request.session['username']=username
          return redirect("Products")
     
     return render (request,"login_cred.html")
def logout_custom(request):
     logout(request)
     request.session.flush()
     return redirect ("login_cred")
def addtoprod(request):
     return render(request,"addtoproduct.html")

def addcontent(request,cust_name):
    print(cust_name)
    cust_name=get_object_or_404(Credentials,id=cust_name) #pk=primary key
    print(cust_name)
    if request.method=="POST":
     username=request.POST['username']
     password=request.POST['password']
     cust_name.Username=username
     cust_name.Password=password
     cust_name.save()
     
    
    
     return redirect('viewers_list')
    return render(request,"Productchecker.html",{'customer_username':cust_name})
        # return redirect('addtoprod')

         

    '''print(cust_name)
    all_data=Credentials.objects.all()
    context={
        'customer_username':cust_name, 
        'data_all':all_data
    }'''
    
     
'''def addcontent1(request):
     return render(request,"Productchecker.html")'''
def viewers_list(request):
     viewers_list=Credentials.objects.all()
     return render(request,"viewers_list.html",{'listofviewers':viewers_list})  
def delete_user(request,cust_name):
     delete_user=get_object_or_404(Credentials,id=cust_name)
     print(delete_user)
     if request.method=="POST":
          delete_user.delete()
          return redirect('viewers_list')
     return render(request,"deleted_users.html",{'data':delete_user})
def form_user(request):
     if request.method == "POST":
          form=CustomerForm(request.POST)
          if form.is_valid():
               form.save()
               messages.success(request,"Customer data has been registered successfully")

              # return redirect('registeration')
     else:
          form=CustomerForm()
     return render(request,"form.html",{'form':form})

def customersearch(request):
    name=request.GET.get("cname")
    if name:
         cust=CustomerDetails.objects.filter(CName=name)
         print(cust)
    else:
         cust=None 
         print(cust)
    return render (request,"form.html",{'custname': cust}) 
def payment(request):
     return render(request,"payment.html")
def finalorder(request):
     return render(request,'orderconfirmation.html')
         




