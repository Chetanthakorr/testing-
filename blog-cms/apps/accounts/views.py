"""
Accounts views — login, logout, password management
"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:home')
    
    error = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next') or 'dashboard:home'
            return redirect(next_url)
        else:
            error = 'Invalid username or password.'
    
    return render(request, 'cms/login.html', {'error': error})


@require_POST
def logout_view(request):
    logout(request)
    return redirect('accounts:login')


@login_required
def profile_view(request):
    return render(request, 'cms/profile.html', {'user': request.user})

