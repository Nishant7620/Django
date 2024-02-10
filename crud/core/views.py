from django.shortcuts import render
from .forms import MarvelForm

# Create your views here.


def crud (request):
    # form = MarvelForm
    if request.method == "POST":
        form = MarvelForm(request.POST)
        if form.is_valid():
            form.save()
        form = MarvelForm()    
    else:
        form = MarvelForm()
    return render(request,'crud/crud.html',{'form':form})