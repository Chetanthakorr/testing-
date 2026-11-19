"""Publishing views"""
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from apps.articles.models import Article
from apps.publishing.engine import publish_article, unpublish_article

app_name = 'publishing'


@login_required
@require_POST
def publish_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    result = publish_article(article, request.user)
    return JsonResponse(result)


@login_required
@require_POST
def unpublish_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    result = unpublish_article(article, request.user)
    return JsonResponse(result)
