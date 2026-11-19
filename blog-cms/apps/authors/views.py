"""Authors views"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import Author


@login_required
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'cms/authors/list.html', {'authors': authors})


@login_required
def author_create(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        bio = request.POST.get('bio', '').strip()
        email = request.POST.get('email', '').strip()
        if name:
            Author.objects.create(name=name, bio=bio, email=email)
            messages.success(request, f'Author "{name}" created.')
    return redirect('authors:list')


@login_required
def author_edit(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.name = request.POST.get('name', author.name).strip()
        author.bio = request.POST.get('bio', author.bio).strip()
        author.email = request.POST.get('email', author.email).strip()
        author.save()
        messages.success(request, 'Author updated.')
        return redirect('authors:list')
    return render(request, 'cms/authors/edit.html', {'author': author})


@login_required
@require_POST
def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    name = author.name
    author.delete()
    messages.success(request, f'Author "{name}" deleted.')
    return redirect('authors:list')
