from django.shortcuts import render

# Create your views here.

def batman(request):
    return render(request,'batman.html')

def superman(request):
    return render(request,'superman.html')    