from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.


def index(request):
    return HttpResponse('Hello Hamed')

def newprod(request):
    return HttpResponse('new products')



