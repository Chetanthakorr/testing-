from django.urls import path
from . import views
app_name = 'media_library'
urlpatterns = [
    path('', views.media_list, name='list'),
    path('upload/', views.media_upload, name='upload'),
    path('<int:pk>/', views.media_detail, name='detail'),
    path('<int:pk>/delete/', views.media_delete, name='delete'),
]
