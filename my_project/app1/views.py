from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def marvel(request):
    return HttpResponse("Spinder")


def DC(request):
    return HttpResponse("superman")
