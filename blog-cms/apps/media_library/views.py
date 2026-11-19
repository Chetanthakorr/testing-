"""Media Library views"""
import os
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib import messages
from django.core.paginator import Paginator
from .models import MediaFile


ALLOWED_TYPES = {'image/jpeg', 'image/png', 'image/webp', 'image/gif', 'image/svg+xml'}
MAX_SIZE_MB = 10


@login_required
def media_list(request):
    q = request.GET.get('q', '')
    qs = MediaFile.objects.all()
    if q:
        qs = qs.filter(filename__icontains=q)
    paginator = Paginator(qs, 24)
    page = paginator.get_page(request.GET.get('page'))
    return render(request, 'cms/media/list.html', {'media_files': page, 'q': q})


@login_required
def media_upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        f = request.FILES['file']
        # Validate
        if f.content_type not in ALLOWED_TYPES:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'error': 'Invalid file type. Upload JPEG, PNG, WebP, GIF or SVG.'}, status=400)
            messages.error(request, 'Invalid file type.')
            return redirect('media_library:list')
        if f.size > MAX_SIZE_MB * 1024 * 1024:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'error': f'File too large. Max {MAX_SIZE_MB}MB.'}, status=400)
            messages.error(request, f'File too large. Max {MAX_SIZE_MB}MB.')
            return redirect('media_library:list')

        alt_text = request.POST.get('alt_text', '')
        caption = request.POST.get('caption', '')
        media = MediaFile.objects.create(
            file=f,
            filename=f.name,
            alt_text=alt_text,
            caption=caption,
            file_size=f.size,
            mime_type=f.content_type,
            uploaded_by=request.user,
        )

        # Also copy to site's images/blog/ directory
        from django.conf import settings
        site_root = settings.CONGOPRIME_SITE_ROOT
        dest = site_root / 'images' / 'blog' / f.name
        if not dest.exists():
            import shutil
            shutil.copy2(media.file.path, str(dest))

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'id': media.pk,
                'url': media.url,
                'filename': media.filename,
                'site_path': media.site_image_path,
            })
        messages.success(request, f'Uploaded: {f.name}')
        return redirect('media_library:list')

    return render(request, 'cms/media/upload.html')


@login_required
@require_POST
def media_delete(request, pk):
    media = get_object_or_404(MediaFile, pk=pk)
    filename = media.filename
    try:
        if media.file and os.path.exists(media.file.path):
            os.remove(media.file.path)
    except Exception:
        pass
    media.delete()
    messages.success(request, f'Deleted: {filename}')
    return redirect('media_library:list')


@login_required
def media_detail(request, pk):
    media = get_object_or_404(MediaFile, pk=pk)
    if request.method == 'POST':
        media.alt_text = request.POST.get('alt_text', media.alt_text)
        media.caption = request.POST.get('caption', media.caption)
        media.save()
        messages.success(request, 'Media updated.')
    return render(request, 'cms/media/detail.html', {'media': media})
