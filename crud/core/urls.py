from django.urls import path
from core import views
urlpatterns = [
    path('',views.crud),
    path('delete /<int:id>/',views.delete,name='delete')
]
