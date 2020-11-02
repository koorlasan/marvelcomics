from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show-results/<title>', views.show_results, name='show_results'),
    path('save/<comic>', views.save_comic, name='save_comic'),
]