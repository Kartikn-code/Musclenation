from django.contrib import admin
from django.urls import path
from .views import login_custom,loginpage,Products,login_cred,registeration,userlogin
from .views import logout_custom,addtoprod,addcontent,viewers_list,delete_user,form_user,customersearch,payment,finalorder
urlpatterns = [
    path('login/',login_custom ,name="login_custom"),
    path('loginpage/',loginpage,name="loginpage"),
    path('Products/',Products,name="Products"),
    path('login_cred/',login_cred,name="login_cred"),
    path('registeration/',registeration,name="registeration"),
    path('user_login/',userlogin,name="userlogin"),
    path('logout_custom/',logout_custom,name="logout_custom"),
    path('add_prod/',addtoprod,name="addtoprod"),
    path('prod_check/<int:cust_name>/',addcontent,name="addcontent"),
    path('viewers_list/',viewers_list,name="viewers_list"),
    path('delete_user/<int:cust_name>/',delete_user,name="delete_user"),
    path('form_user/',form_user,name="form_user"),
    path('find_cust/',customersearch,name="find_customer"),
    path('payment_mode/',payment,name="payment"),
     path('final_order/',finalorder,name="final_order"),

    
    
    
    
    
    
    #path('prod_check/',addcontent,name="addcontent"),



    
    
]