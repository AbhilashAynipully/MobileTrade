from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import RegistrationForm


# Create your views here.

def get_home_page(request):
    return render(request,'../templates/index.html')


def get_login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("You have successfully logged in!"))
            return redirect('home')
        else:
            messages.success(request,("There was an error, please try again"))
            return redirect('login')
    else:
        return render(request,'../templates/login.html')


def get_logout_page(request):
    logout(request)
    messages.success(request,("You have successfully logged out!"))
    return redirect('home')


def get_register_page(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request,("Registration Successful!"))
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request,'../templates/register.html',{'form': form})