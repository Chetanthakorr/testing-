"""Preview views"""
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from apps.articles.models import Article
from apps.publishing.engine import render_article_html


@login_required
def preview_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    html = render_article_html(article)
    return HttpResponse(html, content_type='text/html')
