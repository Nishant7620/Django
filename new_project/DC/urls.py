from django.urls import path
from DC import views

urlpatterns = [
    path('batman/',views.batman)
]