from django.shortcuts import render
from django.urls import path


# Create your views here.

def home(request):
    return render(request, 'home.html')

def add(request):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    
    return render(request, 'result.html', {'result':res})