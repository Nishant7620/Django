from django.urls import path
from toyota import views

urlpatterns = [
    path('fortuner/',views.Fortuner)
]