from django.urls import path
from . import views
app_name = 'publishing'
urlpatterns = [
    path('<int:pk>/publish/', views.publish_view, name='publish'),
    path('<int:pk>/unpublish/', views.unpublish_view, name='unpublish'),
]
