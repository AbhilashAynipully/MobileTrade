from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import RegistrationForm,UserUpdateForm,ProfileUpdateForm
from .models import Profile
from mobiles.models import Mobile, Favourite

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


def get_user_profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id = pk)
        return render(request,"profile.html",{"profile": profile})
    else:
        messages.success(request,("You must be logged in to view this page!"))
        return redirect('login')


def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()

        messages.success(request, 'Your Account was deleted successfully')
        return redirect('home')
    return render(request,'../templates/delete_account.html')


def get_profile_update(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
            
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request,("Your Profile has been updated !"))
                return redirect('home')

        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)
        
        context = {
            'u_form' : u_form,
            'p_form' : p_form
        }

        return render(request,'../templates/profile_update.html', context)

    else:
        messages.success(request,("You must be logged in to view this page!"))
        return redirect('login')


def get_my_mobiles(request):
    if request.user.is_authenticated:
        mobiles = Mobile.objects.filter(seller=request.user)
        return render(request,'../templates/my_mobiles.html',{'mobiles': mobiles})
    
    else:
        messages.success(request,("You must be logged in to view this page!"))
        return redirect('login')


def get_my_favourites(request):
    if request.user.is_authenticated:
        favourites = Favourite.objects.filter(seller=request.user)
        return render(request, '../templates/my_favourites.html', {'favourites':favourites})

    else:
        messages.success(request,("You must be logged in to view this page!"))
        return redirect('login')