from django.urls import path
from . import views
app_name = 'authors'
urlpatterns = [
    path('', views.author_list, name='list'),
    path('create/', views.author_create, name='create'),
    path('<int:pk>/edit/', views.author_edit, name='edit'),
    path('<int:pk>/delete/', views.author_delete, name='delete'),
]
