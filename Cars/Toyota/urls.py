from django.urls import path
from Toyota import views

urlpatterns = [
    path('fortuner/',views.Fortuner)
]