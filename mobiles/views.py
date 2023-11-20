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

