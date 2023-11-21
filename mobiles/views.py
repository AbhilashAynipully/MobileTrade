from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Mobile, Favourite
from . import choices
from .tool import filter_mobiles 
from .forms import MobileAdditionForm

def get_all_mobiles(request):
    mobiles = filter_mobiles(request)

    context = {
        'brand' : choices.BRANDS,
        'mobiles' : mobiles, 
        'values' : request.GET
    }
    return render(request,'../templates/all_mobiles.html',context)


def get_add_mobiles(request):
    if request.user.is_authenticated:
        form = MobileAdditionForm()

        if request.method == 'POST':
            form = MobileAdditionForm(request.POST, request.FILES)

            if form.is_valid():
                mobile = form.save(commit=False)
                mobile.seller = request.user
                mobile.save()
                messages.success(request, 'Your mobile has been added successfully!')
                return redirect('home')
            else:
                messages.error(request, 'Sorry your upload was unsuccessful! Please try again.')
        
        return render(request, '../templates/add_mobiles.html', {'form': form})


def get_delete_mobiles(request, pk):
    if request.user.is_authenticated:
        mobile = get_object_or_404(Mobile, pk=pk)
            
        if request.method == 'POST':
            mobile.delete()
            messages.success(request, 'Your mobile records were deleted successfully')
            return redirect('home')
        
        return render(request, '../templates/delete_mobiles.html',{'mobile': mobile})
    
    else:
        messages.success(request,("You must be logged in to view this page!"))
        return redirect('login')


def get_edit_mobiles(request, pk):
    if request.user.is_authenticated:
        mobile = get_object_or_404(Mobile, pk=pk)
        form = MobileAdditionForm(instance=mobile)
        
        if request.method == 'POST':
            form = MobileAdditionForm(request.POST, request.FILES, instance=mobile)
            if form.is_valid():
                mobile = form.save()
                messages.success(request, 'Your mobile details were updated successfully.')
                return redirect('home')
            else:
                messages.error(request, 'Sorry, details were not updated! Please try again.')
        return render(request, '../templates/edit_mobiles.html',{'form': form})

    else:
        messages.success(request,("You must be logged in to view this page!"))
        return redirect('login')


def delete_favourites(request, pk):
    if request.user.is_authenticated:
        mobile = get_object_or_404(Mobile, pk=pk)
        user = request.user

        if request.method == 'POST':
            favourite = get_object_or_404(
                Favourite, seller=user, mobile=mobile)
            if favourite:
                favourite.delete()
                messages.success(request, 'Removed from favourites')
                return redirect('my-favourites')

        return render(
            request, '../templates/delete_favourites.html', {'mobile': mobile})
    
    else:
        messages.success(request,("You must be logged in to view this page!"))
        return redirect('login')