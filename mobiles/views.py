from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Mobile, Favourite
from . import choices
from .tool import filter_mobiles 

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
                return redirect('my_mobiles', request.user)
            else:
                messages.error(request, 'Sorry your upload was unsuccessful! Please try again.')
        
        return render(request, '../templates/add_mobiles.html', {'form': form})
