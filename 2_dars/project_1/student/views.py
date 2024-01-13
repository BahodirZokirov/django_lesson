from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Name (request):
    return HttpResponse("Bahodir")


def Age (request ):
    return HttpResponse('20')


def City (request):
    return HttpResponse("Samarkand")


def Proff (request):
    return HttpResponse("Programmer")


def Degree (request):
    return HttpResponse("Oliy ma'lumotli")