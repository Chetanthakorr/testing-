"""
Congo Prime Blog CMS — URL configuration
"""
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cms/', include('apps.accounts.urls', namespace='accounts')),
    path('cms/', include('apps.dashboard.urls', namespace='dashboard')),
    path('cms/articles/', include('apps.articles.urls', namespace='articles')),
    path('cms/categories/', include('apps.categories.urls', namespace='categories')),
    path('cms/tags/', include('apps.tags_app.urls', namespace='tags')),
    path('cms/authors/', include('apps.authors.urls', namespace='authors')),
    path('cms/media/', include('apps.media_library.urls', namespace='media_library')),
    path('cms/import/', include('apps.importer.urls', namespace='importer')),
    path('cms/publish/', include('apps.publishing.urls', namespace='publishing')),
    path('cms/preview/', include('apps.preview.urls', namespace='preview')),
    path('cms/history/', include('apps.history.urls', namespace='history')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

