from django.shortcuts import render
from .forms import MarvelForm
from .models import MarvelModel

# Create your views here.


def crud (request):
    # form = MarvelForm
    if request.method == "POST":
        form = MarvelForm(request.POST)
        if form.is_valid():
            form.save()
        mm = MarvelModel.objects.all()    
        form = MarvelForm()    
    else:
        form = MarvelForm()
        mm = MarvelModel.objects.all()  
    return render(request,'crud/crud.html',{'form':form} ,{'mm':mm})