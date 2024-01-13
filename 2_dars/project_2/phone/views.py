from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def Samsung (request):
    return HttpResponse("S22 ultra")



def Iphone (request):
    return HttpResponse ("Iphone 15 pro max")



def Mi (request):
    return HttpResponse("POCO X3 pro")

