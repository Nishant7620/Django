from django.shortcuts import render

# Create your views here.
def Fortuner(request):
    return render(request,'fortuner.html')