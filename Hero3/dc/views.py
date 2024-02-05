from django.shortcuts import render
from .forms import Dc
from .forms import Dc

# Create your views here.

def flash(request):
    dc = Dc()
    if request.method =="POST":
        m =Dc(request.POST)
        if m.is_valid():
            nm = m.cleaned_data['name']
            hn = m.cleaned_data['heroic_name']
            print('Name',nm)
            print('heroic_name',hn)
            mm = Dc(name = nm,heroic_name = hn)
            mm.save()
    else:
        m = Dc()         
    return render(request,'dc/flash.html',{"dc":dc})