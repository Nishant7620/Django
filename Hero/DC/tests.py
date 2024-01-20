from django.test import TestCase
from django.http import HttpResponse

# Create your tests here.

def batman(request):
    return HttpResponse("Batman")

def superman(request):
    return HttpResponse("Superman")    