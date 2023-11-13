from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

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