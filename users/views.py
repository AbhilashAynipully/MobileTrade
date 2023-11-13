from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def get_home_page(request):
    return render(request,'../templates/index.html')


def get_login_page(request):
    return render(request,'../templates/login.html')


def get_logout_page(request):
    pass