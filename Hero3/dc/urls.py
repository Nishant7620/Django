from django.urls import path
from dc import views

urlpatterns = [
    path('flash',views.flash)
]