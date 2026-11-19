from django.urls import path
from . import views
app_name = 'history'
urlpatterns = [
    path('article/<int:pk>/', views.article_history, name='article'),
    path('log/', views.publishing_log, name='log'),
]
