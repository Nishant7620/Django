from django.shortcuts import render
from .forms import MarvelForm
from .models import Marvel

# Create your views here.

def spiderman(request):
    # form = MarvelForm()
    if request.method =="POST":
        form = MarvelForm(request.POST)
        if form.is_valid():
            # n = form.cleaned_data['name']
            # h = form.cleaned_data['heroic_name']
            # print('Name',n)
            # print('Heroic_name',h)
            # m = Marvel(name = n,heroic_name = h)
            form.save()
        mm = Marvel.objects.all()
        form = MarvelForm() 
    else:
        form = MarvelForm()
        mm = Marvel.objects.all()        
    return render(request,'Marvel/spiderman.html',{'form':form})

    