from django.shortcuts import render
from .forms import Dc

# Create your views here.

def flash(request):
    dc = Dc()
    return render(request,'dc/flash.html',{"dc":dc})