from django.urls import path
from . import views
app_name = 'tags'
urlpatterns = [
    path('', views.tag_list, name='list'),
    path('create/', views.tag_create, name='create'),
    path('<int:pk>/delete/', views.tag_delete, name='delete'),
]
