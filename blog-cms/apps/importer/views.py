"""HTML Importer views"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from bs4 import BeautifulSoup

from apps.articles.models import Article
from apps.importer.models import ImportedHTML
from apps.utils import unique_slug


def _extract_article_data(html_content: str) -> dict:
    """
    Extract title, content, excerpt, seo fields from an existing Congo Prime HTML article.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # Title
    h1 = soup.find('h1')
    title_tag = soup.find('title')
    title = ''
    if h1:
        title = h1.get_text(strip=True)
    elif title_tag:
        title = title_tag.get_text(strip=True).split('|')[0].strip()

    # SEO description
    desc_tag = soup.find('meta', attrs={'name': 'description'})
    seo_description = desc_tag['content'] if desc_tag and desc_tag.get('content') else ''

    # SEO title
    seo_title_val = ''
    og_title = soup.find('meta', property='og:title')
    if og_title:
        seo_title_val = og_title.get('content', '')

    # Canonical
    canonical_tag = soup.find('link', rel='canonical')
    canonical = canonical_tag['href'] if canonical_tag and canonical_tag.get('href') else ''

    # Main content: .text div inside .blog-single
    content_div = soup.select_one('.blog-single .text')
    if not content_div:
        content_div = soup.select_one('.sidebar-page-container .text')
    content_html = str(content_div) if content_div else ''

    # Excerpt: first <p>
    excerpt = ''
    if content_div:
        first_p = content_div.find('p')
        if first_p:
            excerpt = first_p.get_text(strip=True)[:300]

    # Featured image
    img_src = ''
    article_img = soup.select_one('.blog-single .image img')
    if article_img:
        img_src = article_img.get('src', '')

    return {
        'title': title,
        'content': content_html,
        'excerpt': excerpt,
        'seo_title': seo_title_val[:70] if seo_title_val else '',
        'seo_description': seo_description[:160] if seo_description else '',
        'canonical_url': canonical,
        'featured_image_src': img_src,
    }


@login_required
def import_view(request):
    preview_data = None
    raw_html = ''
    filename = ''

    if request.method == 'POST':
        action = request.POST.get('action', 'preview')
        raw_html = request.POST.get('html_content', '')
        filename = request.POST.get('filename', '')

        # Handle file upload
        if request.FILES.get('html_file'):
            f = request.FILES['html_file']
            filename = f.name
            raw_html = f.read().decode('utf-8', errors='replace')

        if not raw_html.strip():
            messages.error(request, 'No HTML content provided.')
            return render(request, 'cms/importer/import.html', {})

        extracted = _extract_article_data(raw_html)

        if action == 'preview':
            preview_data = extracted
            preview_data['raw_html'] = raw_html
            preview_data['filename'] = filename

        elif action == 'import':
            title = request.POST.get('title', extracted.get('title', 'Imported Article'))
            slug = unique_slug(Article, title)

            article = Article.objects.create(
                title=title,
                slug=slug,
                content=request.POST.get('content', extracted.get('content', raw_html)),
                excerpt=request.POST.get('excerpt', extracted.get('excerpt', ''))[:500],
                seo_title=request.POST.get('seo_title', extracted.get('seo_title', ''))[:70],
                seo_description=request.POST.get('seo_description', extracted.get('seo_description', ''))[:160],
                canonical_url=request.POST.get('canonical_url', extracted.get('canonical_url', '')),
                status=Article.STATUS_DRAFT,
                created_by=request.user,
            )

            ImportedHTML.objects.create(
                article=article,
                original_filename=filename,
                original_html=raw_html,
                imported_by=request.user,
            )

            messages.success(request, f'Article imported as draft: "{article.title}"')
            return redirect('articles:edit', pk=article.pk)

    return render(request, 'cms/importer/import.html', {
        'preview_data': preview_data,
        'raw_html': raw_html,
        'filename': filename,
    })
