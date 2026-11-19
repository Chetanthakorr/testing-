"""
Articles views — CRUD, publish, schedule, trash, restore
"""
import json
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator

from .models import Article
from .forms import ArticleForm
from apps.history.models import ArticleRevision, PublishingEvent
from apps.publishing.engine import publish_article, unpublish_article, render_article_html
from apps.utils import unique_slug


def _save_revision(article, user, note=''):
    ArticleRevision.objects.create(
        article=article,
        title=article.title,
        content=article.content,
        excerpt=article.excerpt,
        seo_title=article.seo_title,
        seo_description=article.seo_description,
        changed_by=user,
        note=note
    )


@login_required
def article_list(request):
    status_filter = request.GET.get('status', '')
    q = request.GET.get('q', '')
    
    qs = Article.objects.exclude(status='trash').order_by('-updated_at')
    
    if status_filter:
        qs = qs.filter(status=status_filter)
    if q:
        qs = qs.filter(title__icontains=q)
    
    paginator = Paginator(qs, 20)
    page = paginator.get_page(request.GET.get('page'))
    
    return render(request, 'cms/articles/list.html', {
        'articles': page,
        'status_filter': status_filter,
        'q': q,
        'status_choices': Article.STATUS_CHOICES,
    })


@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.created_by = request.user
            if not article.slug:
                article.slug = unique_slug(Article, article.title)
            article.save()
            form.save_m2m()
            _save_revision(article, request.user, note='Created')
            
            action = request.POST.get('action', 'save_draft')
            if action == 'publish':
                result = publish_article(article, request.user)
                if result['success']:
                    messages.success(request, f'Article published: {article.title}')
                else:
                    messages.error(request, f'Publish failed: {", ".join(result["errors"])}')
            elif action == 'schedule':
                article.status = Article.STATUS_SCHEDULED
                article.save(update_fields=['status'])
                PublishingEvent.objects.create(
                    article=article, action=PublishingEvent.ACTION_SCHEDULE,
                    performed_by=request.user, success=True
                )
                messages.success(request, f'Article scheduled: {article.title}')
            else:
                messages.success(request, f'Draft saved: {article.title}')
            
            return redirect('articles:edit', pk=article.pk)
    else:
        form = ArticleForm()
    
    return render(request, 'cms/articles/edit.html', {
        'form': form,
        'article': None,
        'is_create': True,
    })


@login_required
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            _save_revision(article, request.user, note='Edited')
            article = form.save(commit=False)
            if not article.slug:
                article.slug = unique_slug(Article, article.title, exclude_pk=pk)
            article.save()
            form.save_m2m()
            
            action = request.POST.get('action', 'save_draft')
            if action == 'publish':
                result = publish_article(article, request.user)
                if result['success']:
                    messages.success(request, f'Article published successfully.')
                else:
                    messages.error(request, f'Publish failed: {", ".join(result["errors"])}')
            elif action == 'unpublish':
                result = unpublish_article(article, request.user)
                if result['success']:
                    messages.success(request, 'Article unpublished.')
                else:
                    messages.error(request, f'Unpublish failed: {", ".join(result["errors"])}')
            elif action == 'schedule':
                article.status = Article.STATUS_SCHEDULED
                article.save(update_fields=['status'])
                PublishingEvent.objects.create(
                    article=article, action=PublishingEvent.ACTION_SCHEDULE,
                    performed_by=request.user, success=True
                )
                messages.success(request, 'Article scheduled.')
            else:
                article.status = Article.STATUS_DRAFT
                article.save(update_fields=['status'])
                messages.success(request, 'Draft saved.')
            
            return redirect('articles:edit', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    
    revisions = article.revisions.order_by('-changed_at')[:10]
    return render(request, 'cms/articles/edit.html', {
        'form': form,
        'article': article,
        'is_create': False,
        'revisions': revisions,
    })


@login_required
@require_POST
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.soft_delete()
    PublishingEvent.objects.create(
        article=article, action=PublishingEvent.ACTION_DELETE,
        performed_by=request.user, success=True
    )
    messages.success(request, f'"{article.title}" moved to trash.')
    return redirect('articles:list')


@login_required
def article_trash(request):
    articles = Article.objects.filter(status='trash').order_by('-deleted_at')
    return render(request, 'cms/articles/trash.html', {'articles': articles})


@login_required
@require_POST
def article_restore(request, pk):
    article = get_object_or_404(Article, pk=pk, status='trash')
    article.restore()
    PublishingEvent.objects.create(
        article=article, action=PublishingEvent.ACTION_RESTORE,
        performed_by=request.user, success=True
    )
    messages.success(request, f'"{article.title}" restored to drafts.')
    return redirect('articles:trash')


@login_required
@require_POST
def article_publish_ajax(request, pk):
    article = get_object_or_404(Article, pk=pk)
    result = publish_article(article, request.user)
    return JsonResponse(result)


@login_required
def article_slug_check(request):
    """AJAX: check if slug is unique."""
    slug = request.GET.get('slug', '')
    pk = request.GET.get('pk')
    qs = Article.objects.filter(slug=slug)
    if pk:
        qs = qs.exclude(pk=pk)
    return JsonResponse({'available': not qs.exists()})

