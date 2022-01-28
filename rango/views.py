from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict) # <a href='/rango/about/'>About</a>

def about(request):
    return render(request, 'rango/about.html') # <a href='/rango/'>Index</a>