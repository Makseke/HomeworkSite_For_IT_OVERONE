from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Хэй, оно работает!</h1><p>На удивление</p>")