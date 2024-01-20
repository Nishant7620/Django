from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Fortuner (request):
    return HttpResponse("this isFortuner car")