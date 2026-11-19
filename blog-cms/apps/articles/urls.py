from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('create/', views.article_create, name='create'),
    path('<int:pk>/edit/', views.article_edit, name='edit'),
    path('<int:pk>/delete/', views.article_delete, name='delete'),
    path('<int:pk>/restore/', views.article_restore, name='restore'),
    path('<int:pk>/publish/', views.article_publish_ajax, name='publish_ajax'),
    path('trash/', views.article_trash, name='trash'),
    path('slug-check/', views.article_slug_check, name='slug_check'),
]

