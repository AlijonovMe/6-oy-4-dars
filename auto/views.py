from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404
from .models import *

def home(request: WSGIRequest):
    brands = Brand.objects.all()
    cars = Cars.objects.all()
    context = {
        'brands': brands,
        'cars': cars
    }

    return render(request, 'index.html', context)

def brands(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    cars = Cars.objects.filter(brand=brand)
    context = {
        'brands': brand,
        'cars': cars
    }

    return render(request, 'brands.html', context)
