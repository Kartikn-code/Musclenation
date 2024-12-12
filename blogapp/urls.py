from django.contrib import admin
from django.urls import path
from .views import a1
urlpatterns = [
    path('blog/', a1,name="a1"),
   
]