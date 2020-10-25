from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save/<comic>', views.save_comic, name='save_comic'),
]