from django.shortcuts import render

# Create your views here.

def loki(request):
    context={"God":"Mischief"}
    return render(request,'marvel/loki.html',context)