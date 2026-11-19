"""
Dashboard views
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.articles.models import Article
from apps.media_library.models import MediaFile
from apps.categories.models import Category
from apps.authors.models import Author
from apps.history.models import PublishingEvent


@login_required
def home(request):
    context = {
        'total_articles': Article.objects.exclude(status='trash').count(),
        'published_count': Article.objects.filter(status='published').count(),
        'draft_count': Article.objects.filter(status='draft').count(),
        'scheduled_count': Article.objects.filter(status='scheduled').count(),
        'media_count': MediaFile.objects.count(),
        'category_count': Category.objects.count(),
        'author_count': Author.objects.count(),
        'recent_articles': Article.objects.exclude(status='trash').order_by('-updated_at')[:5],
        'recent_events': PublishingEvent.objects.order_by('-timestamp')[:8],
    }
    return render(request, 'cms/dashboard.html', context)

