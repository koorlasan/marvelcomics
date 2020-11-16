from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('show-results/<title>', views.show_results, name='show_results'),
    #path('save/<comic>', views.save_comic, name='save_comic'),
    path('comic/<title>', views.ComicDetailView.as_view(), name='comic-info'),
]