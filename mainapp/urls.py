from django.contrib import admin
from django.urls import path
from .views import add,about,display

urlpatterns = [
    path('HOME/', add,name="add"),
    path('about/', about,name="about"),
    path('display/<int:user_id>/', display,name="display"),
]