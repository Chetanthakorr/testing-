from django.urls import path
from . import views
app_name = 'preview'
urlpatterns = [
    path('<int:pk>/', views.preview_article, name='preview'),
]
