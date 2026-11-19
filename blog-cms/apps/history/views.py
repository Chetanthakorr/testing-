"""History views"""
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.articles.models import Article
from apps.history.models import ArticleRevision, PublishingEvent


@login_required
def article_history(request, pk):
    article = get_object_or_404(Article, pk=pk)
    revisions = article.revisions.order_by('-changed_at')
    events = article.publishing_events.order_by('-timestamp')
    return render(request, 'cms/history/article_history.html', {
        'article': article,
        'revisions': revisions,
        'events': events,
    })


@login_required
def publishing_log(request):
    events = PublishingEvent.objects.order_by('-timestamp').select_related('article', 'performed_by')[:100]
    return render(request, 'cms/history/publishing_log.html', {'events': events})
