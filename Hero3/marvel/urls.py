from django.urls import path
from marvel import views

urlpatterns = [
    path('loki',views.loki)
]