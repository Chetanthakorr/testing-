"""Tags views"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import Tag
from apps.utils import slugify


@login_required
def tag_list(request):
    tags = Tag.objects.all().order_by('name')
    return render(request, 'cms/tags/list.html', {'tags': tags})


@login_required
def tag_create(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if name:
            slug = slugify(name)
            Tag.objects.get_or_create(slug=slug, defaults={'name': name})
            messages.success(request, f'Tag "{name}" created.')
    return redirect('tags:list')


@login_required
@require_POST
def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    name = tag.name
    tag.delete()
    messages.success(request, f'Tag "{name}" deleted.')
    return redirect('tags:list')
