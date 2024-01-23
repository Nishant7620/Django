from django.shortcuts import render

# Create your views here.
def batman(request):
    context = {"numbers":[1,2,3,4,5]}
    return render(request,'Dc/batman.html',context)