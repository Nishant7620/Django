from django.urls import path
from Marvel import views
urlpatterns = [
    path('spiderman/',views.spiderman)
]