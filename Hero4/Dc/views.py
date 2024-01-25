from django.shortcuts import render
from Dc.models import Dc

# Create your views here.
def batman(request):
    dc = Dc.objects.all()
    
    return render(request,'Dc/batman.html',{"hero":dc})