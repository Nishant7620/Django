from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def batman(request):
    return HttpResponse("batman")