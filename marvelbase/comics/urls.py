from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('show-results/<title>', views.show_results, name='show_results'),
    path('comic-info/<int:id>/', views.comic_info, name='comic_info'),
    path('my-comics/', views.my_comics, name='my_comics'),
    path('my-comics/edit-comic/<int:id>/', views.edit, name='edit'),
    path('my-comics/delete/<int:id>/', views.delete, name='delete'),
]
