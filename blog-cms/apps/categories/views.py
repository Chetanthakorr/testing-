"""Categories views"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import Category
from apps.utils import slugify


@login_required
def category_list(request):
    categories = Category.objects.all().order_by('name')
    return render(request, 'cms/categories/list.html', {'categories': categories})


@login_required
def category_create(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        slug = request.POST.get('slug', '').strip() or slugify(name)
        description = request.POST.get('description', '').strip()
        if name:
            cat, created = Category.objects.get_or_create(slug=slug, defaults={'name': name, 'description': description})
            if created:
                messages.success(request, f'Category "{name}" created.')
            else:
                messages.warning(request, f'Category with slug "{slug}" already exists.')
        return redirect('categories:list')
    return render(request, 'cms/categories/list.html', {'categories': Category.objects.all()})


@login_required
@require_POST
def category_delete(request, pk):
    cat = get_object_or_404(Category, pk=pk)
    name = cat.name
    cat.delete()
    messages.success(request, f'Category "{name}" deleted.')
    return redirect('categories:list')
