from django.urls import path
from Marvel import views

urlpatterns = [
    path('marvel/',views.spiderman)
]