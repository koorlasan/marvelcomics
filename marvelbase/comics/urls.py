from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('show-results/<title>', views.show_results, name='show_results'),
    path('comic-info/<int:id>/', views.comic_info, name='comic_info'),
    path('my-comics/', views.my_comics, name='my_comics'),
    # path('edit/', views.edit, name='edit_comic'),
    # path('delete/', views.delete, name='delete'),
]
