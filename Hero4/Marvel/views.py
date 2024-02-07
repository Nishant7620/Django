from django.shortcuts import render
from .forms import MarvelForm

# Create your views here.

def spiderman(request):
    s = MarvelForm()
    return render(request,'Marvel/spiderman.html',{'s':s})

    