from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest
from .models import Products
# Create your views here.


def index(request):
   products =  Products.objects.all()
   return render(request, 'index.html', {'my_products': products})


def newprod(request):
    return HttpResponse('new products')