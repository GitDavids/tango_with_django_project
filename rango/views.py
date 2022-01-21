from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
    """request: HttpRequest object from django.http"""
    return HttpResponse('Rango says hey there partner!')