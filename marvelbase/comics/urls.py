from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('show-results/<title>', views.show_results, name='show_results'),
    path('comic-info/', views.comic_info, name='comic_info')
    # path('save/<comic>', views.save_comic, name='save_comic'),
]
