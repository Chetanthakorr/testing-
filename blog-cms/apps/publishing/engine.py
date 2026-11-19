"""
Congo Prime Blog CMS — Publishing Engine

Responsibilities:
1. Validate article before publish
2. Render article to HTML using existing Congo Prime templates
3. Write generated HTML to d:\prime-main\ directory
4. Update blog.html listing page
5. Update _redirects and server.js routing tables
6. Record publishing events in the audit log
"""
import os
import re
import shutil
import tempfile
from datetime import datetime
from pathlib import Path

from django.conf import settings
from django.utils import timezone

SITE_ROOT = Path(settings.CONGOPRIME_SITE_ROOT)

# Existing blog images in Congo Prime site
BLOG_IMAGE_BASE = '/images/blog/'

# Social SVGs (reused from existing templates)
INSTAGRAM_SVG = '<svg class="social-svg" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.406-11.845a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881z"/></svg>'
FACEBOOK_SVG = '<svg class="social-svg" viewBox="0 0 24 24" aria-hidden="true"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>'
YOUTUBE_SVG = '<svg class="social-svg" viewBox="0 0 24 24" aria-hidden="true"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>'
LINKEDIN_SVG = '<svg class="social-svg" viewBox="0 0 24 24" aria-hidden="true"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 1 1 0-4.124 2.062 2.062 0 0 1 0 4.124zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.225 0z"/></svg>'

SOCIAL_LINKS_HTML = f'''<ul class="clearfix">
    <li>Stay Connected :</li>
    <li><a href="https://www.instagram.com/congoprimeconstructionsarl/" target="_blank" rel="noopener noreferrer" aria-label="Instagram">{INSTAGRAM_SVG}</a></li>
    <li><a href="https://www.facebook.com/profile.php?id=61595428409081" target="_blank" rel="noopener noreferrer" aria-label="Facebook">{FACEBOOK_SVG}</a></li>
    <li><a href="https://www.youtube.com/@CongoPrimeConstructionSARL" target="_blank" rel="noopener noreferrer" aria-label="YouTube">{YOUTUBE_SVG}</a></li>
    <li><a href="https://www.linkedin.com/company/congo-prime-construction-sarl/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">{LINKEDIN_SVG}</a></li>
</ul>'''

SOCIAL_LINKS_FOOTER_HTML = f'''<ul class="social-icon-two">
    <li><a href="https://www.instagram.com/congoprimeconstructionsarl/" target="_blank" rel="noopener noreferrer" aria-label="Instagram">{INSTAGRAM_SVG}</a></li>
    <li><a href="https://www.facebook.com/profile.php?id=61595428409081" target="_blank" rel="noopener noreferrer" aria-label="Facebook">{FACEBOOK_SVG}</a></li>
    <li><a href="https://www.youtube.com/@CongoPrimeConstructionSARL" target="_blank" rel="noopener noreferrer" aria-label="YouTube">{YOUTUBE_SVG}</a></li>
    <li><a href="https://www.linkedin.com/company/congo-prime-construction-sarl/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">{LINKEDIN_SVG}</a></li>
</ul>'''

HEADER_HTML = f'''<header class="main-header header-style-five">
  <div class="header-top">
    <div class="auto-container">
      <div class="inner-container clearfix">
        <div class="top-left"></div>
        <div class="top-right clearfix">
          <div class="social-icon">
            {SOCIAL_LINKS_HTML}
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="main-box">
    <div class="auto-container">
      <div class="outer-container clearfix">
        <div class="logo-box">
          <div class="logo"><a href="index.html"><img src="images/congoprime construction.svg" width="100%" alt="Congo Prime Construction"></a></div>
        </div>
        <div class="nav-outer clearfix">
          <nav class="main-menu">
            <div class="navbar-header">
              <button type="button" class="navbar-toggle" aria-label="Toggle navigation" data-toggle="collapse" data-target=".navbar-collapse">
                <span class="icon-bar"></span><span class="icon-bar"></span><span class="icon-bar"></span>
              </button>
            </div>
            <div class="navbar-collapse collapse clearfix">
              <ul class="navigation clearfix">
                <li><a href="index.html">Home</a></li>
                <li><a href="about.html">About Us</a></li>
                <li class="dropdown"><a href="services.html">Services</a>
                  <ul>
                    <li><a href="Project-Planning-Development.html">Project Planning &amp; Development</a></li>
                    <li><a href="Design-Build-Turnkey-Solutions.html">Design &amp; Build / Turnkey Solutions</a></li>
                    <li><a href="Civil-Structural-Works.html">Civil &amp; Structural Works</a></li>
                    <li><a href="MEP.html">MEP Solutions</a></li>
                    <li><a href="Site-Preparation-Infrastructure-Enablement.html">Site Preparation &amp; Infrastructure Enablement</a></li>
                    <li><a href="Interior-Design-Fit-out-Finishing.html">Interior Design, Fit-out &amp; Finishing</a></li>
                  </ul>
                </li>
                <li class="dropdown"><a href="projects.html">Projects</a>
                  <ul>
                    <li><a href="Commercial-projects.html">Commercial</a></li>
                    <li><a href="Residential-projects.html">Residential</a></li>
                    <li><a href="Industrial-projects.html">Industrial</a></li>
                    <li><a href="Hospitality-Projects.html">Hospitality</a></li>
                    <li><a href="Reconstruction-projects.html">Reconstruction</a></li>
                  </ul>
                </li>
                <li class="current"><a href="blog.html">Blog</a></li>
                <li><a href="contact-2.html">Contact</a></li>
              </ul>
            </div>
          </nav>
        </div>
      </div>
    </div>
  </div>
</header>'''

FOOTER_HTML = f'''<footer class="main-footer" style="background-image:url(images/background/6.webp)">
  <div class="auto-container">
    <div class="upper-box">
      <ul class="list-style-one clearfix">
        <li><span class="icon flaticon-pin"></span>Avenue Lumumba, Opp. Restaurant italien,<br>Casa Mia, Lubumbashi, DRC</li>
        <li><span class="icon flaticon-envelope-1"></span>Email us : <br><a class="contact-link" href="mailto:contact@congoprime.com">contact@congoprime.com</a></li>
        <li><span class="icon flaticon-technology-2"></span>Call us : <br><a class="contact-link" href="tel:+243979446666">+243 979 446 666</a></li>
      </ul>
    </div>
    <div class="widgets-section">
      <div class="row clearfix">
        <div class="big-column col-md-6 col-sm-12 col-xs-12">
          <div class="row clearfix">
            <div class="footer-column col-md-7 col-sm-6 col-xs-12">
              <div class="footer-widget logo-widget">
                <div class="logo"><a href="index.html"><img loading="lazy" decoding="async" src="images/footer-logo.webp" alt="Congo Prime Construction"></a></div>
                <div class="text">Congo Prime is a construction company based in Lubumbashi, DRC, delivering industrial, commercial, hospitality and residential projects.</div>
                {SOCIAL_LINKS_FOOTER_HTML}
              </div>
            </div>
            <div class="footer-column col-md-5 col-sm-6 col-xs-12">
              <div class="footer-widget links-widget"><h2>Quick Links</h2>
                <ul class="list">
                  <li><a href="index.html">Home</a></li>
                  <li><a href="about.html">About Us</a></li>
                  <li><a href="services.html">Services</a></li>
                  <li><a href="projects.html">Projects</a></li>
                  <li><a href="blog.html">Blog</a></li>
                  <li><a href="contact-2.html">Contact Us</a></li>
                </ul>
              </div>
            </div>
          </div>
        </div>
        <div class="big-column col-md-6 col-sm-12 col-xs-12">
          <div class="row clearfix">
            <div class="footer-column col-md-6 col-sm-6 col-xs-12">
              <div class="footer-widget links-widget"><h2>Our Services</h2>
                <ul class="list">
                  <li><a href="Project-Planning-Development.html">Project Planning &amp; Development</a></li>
                  <li><a href="Design-Build-Turnkey-Solutions.html">Design &amp; Build / Turnkey Solutions</a></li>
                  <li><a href="Civil-Structural-Works.html">Civil &amp; Structural Works</a></li>
                  <li><a href="MEP.html">MEP Solutions</a></li>
                  <li><a href="Site-Preparation-Infrastructure-Enablement.html">Site Preparation &amp; Infrastructure Enablement</a></li>
                  <li><a href="Interior-Design-Fit-out-Finishing.html">Interior Design, Fit-out &amp; Finishing</a></li>
                </ul>
              </div>
            </div>
            <div class="footer-column col-md-6 col-sm-6 col-xs-12">
              <div class="footer-widget links-widget"><h2>Projects</h2>
                <ul class="list">
                  <li><a href="Commercial-projects.html">Commercial Projects</a></li>
                  <li><a href="Residential-projects.html">Residential Projects</a></li>
                  <li><a href="Industrial-projects.html">Industrial Projects</a></li>
                  <li><a href="Hospitality-Projects.html">Hospitality Projects</a></li>
                  <li><a href="Reconstruction-projects.html">Reconstruction Projects</a></li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="auto-container"><div class="row clearfix">
      <div class="column col-md-6 col-sm-12 col-xs-12"><div class="copyright">Copyright &copy; HOLYTECH 2026. All rights reserved.</div></div>
    </div></div>
  </div>
</footer>'''


def _escape_html(text: str) -> str:
    return (text.replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;'))


def _format_date(dt) -> str:
    if dt is None:
        return ''
    if hasattr(dt, 'strftime'):
        return dt.strftime('%-d %b %Y') if os.name != 'nt' else dt.strftime('%d %b %Y').lstrip('0')
    return str(dt)


def render_article_html(article) -> str:
    """
    Generate a complete, standalone HTML file for the article,
    matching the Congo Prime article template exactly.
    """
    pub_date = article.published_at or article.updated_at or article.created_at
    formatted_date = _format_date(pub_date)

    # SEO & meta
    seo_title = _escape_html(article.effective_seo_title)
    seo_description = _escape_html(article.seo_description or article.excerpt or '')
    canonical = article.effective_canonical
    article_title = _escape_html(article.title)

    # Image
    if article.featured_image:
        img_src = article.featured_image.site_image_path or f'images/blog/{article.featured_image.filename}'
        img_alt = _escape_html(article.featured_image_alt or article.featured_image.alt_text or article_title)
    else:
        img_src = 'images/logo-2.webp'
        img_alt = article_title

    og_image_url = f'https://congoprime.com/{img_src}'
    if article.og_image:
        og_image_url = f'https://congoprime.com/{article.og_image.site_image_path}'

    # Author
    author_name = article.author.name if article.author else 'Congo Prime'

    # Categories
    categories_html = ''
    for cat in article.categories.all():
        cat_slug = _escape_html(cat.slug)
        cat_name = _escape_html(cat.name)
        categories_html += f'<li><a href="blog.html?category={cat_slug}">{cat_name}</a></li>\n'

    # Tags
    tags_html = ''
    for tag in article.tags.all():
        tag_slug = _escape_html(tag.slug)
        tag_name = _escape_html(tag.name)
        tags_html += f'<a href="blog.html?q={tag_slug}">{tag_name}</a>\n'

    # Recent posts sidebar — query 3 most recent published articles (excluding this one)
    from apps.articles.models import Article as ArticleModel
    recent_posts = ArticleModel.objects.filter(
        status=ArticleModel.STATUS_PUBLISHED
    ).exclude(pk=article.pk).order_by('-published_at')[:3]

    recent_posts_html = ''
    for rp in recent_posts:
        rp_title = _escape_html(rp.title)
        rp_url = f'/blog/{rp.slug}'
        rp_img = rp.featured_image.site_image_path if rp.featured_image else 'images/logo-2.webp'
        rp_img_alt = _escape_html(rp.featured_image_alt or rp.title)
        rp_date = _format_date(rp.published_at)
        recent_posts_html += f'''            <article class="post">
              <figure class="post-thumb"><a href="{rp_url}"><img loading="lazy" decoding="async" src="{rp_img}" alt="{rp_img_alt}"></a></figure>
              <div class="text"><a href="{rp_url}">{rp_title}</a></div>
              <div class="post-info">{rp_date}</div>
            </article>\n'''

    # Schema JSON-LD
    published_iso = pub_date.isoformat() if pub_date else ''
    schema_blogposting = f'''{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{article.effective_seo_title}",
  "description": "{article.seo_description or article.excerpt or ''}",
  "url": "{canonical}",
  "image": "{og_image_url}",
  "datePublished": "{published_iso[:10] if published_iso else ''}",
  "dateModified": "{article.updated_at.isoformat()[:10] if article.updated_at else ''}",
  "author": {{
    "@type": "Organization",
    "name": "Congo Prime Construction",
    "url": "https://congoprime.com/"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "Congo Prime Construction",
    "url": "https://congoprime.com/",
    "logo": {{
      "@type": "ImageObject",
      "url": "https://congoprime.com/images/congoprime construction.svg"
    }}
  }},
  "mainEntityOfPage": {{
    "@type": "WebPage",
    "@id": "{canonical}"
  }}
}}'''

    schema_breadcrumb = f'''{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://congoprime.com/"}},
    {{"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://congoprime.com/blog.html"}},
    {{"@type": "ListItem", "position": 3, "name": "{article.title}"}}
  ]
}}'''

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<base href="/">
<title>{seo_title}</title>
<meta name="description" content="{seo_description}">
<link rel="canonical" href="{canonical}">
<meta property="og:locale" content="en_US">
<meta property="og:type" content="article">
<meta property="article:published_time" content="{published_iso}">
<meta property="og:site_name" content="Congo Prime Construction">
<meta property="og:title" content="{_escape_html(article.title)}">
<meta property="og:description" content="{seo_description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image_url}">
<meta property="og:image:alt" content="{img_alt}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{_escape_html(article.title)}">
<meta name="twitter:description" content="{seo_description}">
<meta name="twitter:image" content="{og_image_url}">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="css/bootstrap.css" rel="stylesheet">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital@1&family=Open+Sans:wght@300;400;700&family=Playfair+Display:ital,wght@1,700&family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
<link href="css/font-awesome.css" rel="stylesheet">
<link href="css/flaticon.css" rel="stylesheet">
<link href="css/style.css" rel="stylesheet">
<link href="css/responsive.css" rel="stylesheet">
<link href="css/social-sharing.css" rel="stylesheet">
<link rel="shortcut icon" href="images/favicon-icon.png" type="image/x-icon">
<link rel="icon" href="images/favicon-icon.png" type="image/x-icon">
<script type="application/ld+json">
{schema_blogposting}
</script>
<script type="application/ld+json">
{schema_breadcrumb}
</script>
</head>
<body>
<div class="page-wrapper">
<div class="preloader"></div>
{HEADER_HTML}
<main id="main-content">

<section class="page-title" style="background-image:url(images/background/12.webp)">
  <div class="auto-container">
    <h1>{article_title}</h1>
    <ul class="page-breadcrumb">
      <li><a href="index.html">Home</a></li>
      <li><a href="blog.html">Blog</a></li>
      <li>{article_title}</li>
    </ul>
  </div>
</section>

<div class="sidebar-page-container">
  <div class="auto-container">
    <div class="row clearfix">
      <div class="content-side col-lg-9 col-md-8 col-sm-12 col-xs-12">
        <div class="blog-single padding-right">
          <div class="inner-box">
            <div class="image">
              <img loading="lazy" decoding="async" src="{img_src}" alt="{img_alt}">
            </div>
            <div class="lower-content">
              <div class="upper-box clearfix">
                <div class="posted-date pull-left">Updated: {formatted_date}</div>
                <ul class="post-meta pull-right">
                  <li>By: {_escape_html(author_name)}</li>
                  {categories_html}
                </ul>
              </div>
              <div class="blog-share" data-blog-share aria-label="Share this article"></div>
              <div class="lower-box">
                <h3>{article_title}</h3>
                <div class="text">
{article.content}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="sidebar-side col-lg-3 col-md-4 col-sm-12 col-xs-12">
        <aside class="sidebar">
          <div class="sidebar-widget search-box">
            <form class="blog-search-form" method="get" action="blog.html" role="search">
              <div class="form-group">
                <input type="search" name="q" placeholder="Enter Search Keywords" aria-label="Search blog">
                <button type="submit" aria-label="Search"><span class="icon fa fa-search"></span></button>
              </div>
            </form>
          </div>
          <div class="sidebar-widget sidebar-blog-category">
            <div class="sidebar-title"><h2>Categories</h2></div>
            <ul class="cat-list">
              <li><a href="blog.html">All Blogs</a></li>
              <li><a href="blog.html?category=construction">Construction</a></li>
              <li><a href="blog.html?category=infrastructure">Infrastructure</a></li>
              <li><a href="blog.html?category=architecture">Architecture</a></li>
              <li><a href="blog.html?category=interior-design">Interior Design</a></li>
              <li><a href="blog.html?category=hospitality">Hospitality</a></li>
              <li><a href="blog.html?category=residential">Residential</a></li>
              <li><a href="blog.html?category=commercial">Commercial</a></li>
            </ul>
          </div>
          <div class="sidebar-widget popular-posts">
            <div class="sidebar-title"><h2>Recent Blogs</h2></div>
{recent_posts_html}
          </div>
          <div class="sidebar-widget popular-tags">
            <div class="sidebar-title"><h2>Tags</h2></div>
{tags_html}
          </div>
        </aside>
      </div>
    </div>
  </div>
</div>

</main>
{FOOTER_HTML}
</div>

<div class="scroll-to-top scroll-to-target" data-target="html"><span class="fa fa-arrow-up"></span></div>
<script src="js/jquery.js"></script>
<script src="js/bootstrap.min.js"></script>
<script src="js/appear.js"></script>
<script src="js/script.js?v=20261016"></script>
<script src="js/social-sharing.js"></script>
</body>
</html>'''
    return html


def render_blog_listing_html(articles) -> str:
    """
    Regenerate the blog.html listing page with published articles.
    Preserves full page structure from existing blog.html.
    """
    # Build article cards
    cards_html = ''
    for article in articles:
        pub_date = article.published_at or article.created_at
        formatted_date = _format_date(pub_date)
        article_title = _escape_html(article.title)
        article_url = f'/blog/{article.slug}'

        if article.featured_image:
            img_src = article.featured_image.site_image_path
            img_alt = _escape_html(article.featured_image_alt or article.featured_image.alt_text or article.title)
        else:
            img_src = 'images/logo-2.webp'
            img_alt = article_title

        # Categories for data-categories and display
        cat_slugs = ' '.join(c.slug for c in article.categories.all())
        cats_display = ''
        for cat in article.categories.all():
            cats_display += f'<li><a href="blog.html?category={_escape_html(cat.slug)}">{_escape_html(cat.name)}</a></li>\n'

        # Tags and search terms for data-search
        tag_names = ' '.join(t.name for t in article.tags.all())
        excerpt = _escape_html(article.excerpt or '')

        cards_html += f'''                    <div class="news-block-three col-md-6 col-sm-12 col-xs-12 blog-card" data-categories="{cat_slugs}" data-search="{_escape_html(article.title)} {_escape_html(tag_names)}">
                        <div class="inner-box">
                            <div class="image">
                                <a href="{article_url}"><img loading="lazy" decoding="async" src="{img_src}" alt="{img_alt}" /></a>
                            </div>
                            <div class="lower-content">
                                <div class="upper-box clearfix">
                                    <div class="posted-date pull-left">{formatted_date}</div>
                                    <ul class="post-meta pull-right">
                                        <li>By: {_escape_html(article.author.name if article.author else 'Author')}</li>
                                        {cats_display}
                                    </ul>
                                </div>
                                <div class="lower-box">
                                    <h3><a href="{article_url}">{article_title}</a></h3>
                                    <div class="text">{excerpt}</div>
                                    <a href="{article_url}" class="theme-btn btn-style-one read-more">Read more<span class="sr-only"> about {article_title}</span></a>
                                    <button type="button" class="blog-card-share" data-share-card data-share-url="https://congoprime.com{article_url}" data-share-title="{article_title}"><span class="fa fa-share-alt" aria-hidden="true"></span> Share</button>
                                </div>
                            </div>
                        </div>
                    </div>\n'''

    blog_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Construction &amp; Design Insights in DRC | Congo Prime Blog</title>
<!-- SEO metadata -->
<link rel="canonical" href="https://congoprime.com/blog.html">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Congo Prime Construction">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="Construction &amp; Design Insights in DRC | Congo Prime Blog">
<meta property="og:description" content="Read Congo Prime insights on construction, infrastructure, housing design, interiors, permits and resilient building across Lubumbashi and the DRC.">
<meta property="og:url" content="https://congoprime.com/blog.html">
<meta property="og:image" content="https://congoprime.com/images/logo-2.webp">
<meta property="og:image:alt" content="Congo Prime Construction">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Construction &amp; Design Insights in DRC | Congo Prime Blog">
<meta name="twitter:description" content="Read Congo Prime insights on construction, infrastructure, housing design, interiors, permits and resilient building across Lubumbashi and the DRC.">
<meta name="twitter:image" content="https://congoprime.com/images/logo-2.webp">
<!-- Stylesheets -->
<link href="css/bootstrap.css" rel="stylesheet">
<link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lora:ital@1&family=Open+Sans:wght@300;400;700&family=Playfair+Display:ital,wght@1,700&family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link href="css/font-awesome.css" rel="stylesheet">
    <link href="css/flaticon.css" rel="stylesheet">
    <link href="css/style.css" rel="stylesheet">
<link href="css/responsive.css" rel="stylesheet">
<link href="css/social-sharing.css" rel="stylesheet">

<link rel="shortcut icon" href="images/favicon-icon.png" type="image/x-icon">
<link rel="icon" href="images/favicon-icon.png" type="image/x-icon">
<!-- Responsive -->
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Read Congo Prime insights on construction, infrastructure, housing design, interiors, permits and resilient building across Lubumbashi and the DRC.">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Construction & Design Insights in DRC | Congo Prime Blog",
  "url": "https://congoprime.com/blog.html",
  "description": "Read Congo Prime insights on construction, infrastructure, housing design, interiors, permits and resilient building across Lubumbashi and the DRC.",
  "isPartOf": {{
    "@id": "https://congoprime.com/#website"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
      {{"@type":"ListItem","position":1,"name":"Home","item":"https://congoprime.com/"}},
      {{"@type":"ListItem","position":2,"name":"Blog","item":"https://congoprime.com/blog.html"}}
  ]
}}
</script>
</head>

<body>

<div class="page-wrapper">
 \t
    <!-- Preloader -->
    <div class="preloader"></div>
 \t
   <!-- Main Header / Header Style Five-->
    {HEADER_HTML}

    <!-- Sticky Header -->
    <div class="sticky-header">
        <div class="auto-container">
                <div class="sticky-inner-container clearfix">
                    <div class="logo pull-left">
                        <a href="index.html" class="img-responsive"><img src="images/logo-2.webp" alt="Congo Prime Construction" title=""></a>
                    </div>
                    <div class="right-col pull-right">
                        <nav class="main-menu">
                            <div class="navbar-collapse collapse clearfix">
                                <ul class="navigation clearfix">
                                    <li><a href="index.html">Home</a></li>
                                    <li><a href="about.html">About Us</a></li>
                                    <li class="dropdown"><a href="services.html">Services</a>
                                        <ul>
                                            <li><a href="Project-Planning-Development.html">Project Planning &amp; Development</a></li>
                                            <li><a href="Design-Build-Turnkey-Solutions.html">Design &amp; Build / Turnkey Solutions</a></li>
                                            <li><a href="Civil-Structural-Works.html">Civil &amp; Structural Works</a></li>
                                            <li><a href="MEP.html">MEP Solutions</a></li>
                                            <li><a href="Site-Preparation-Infrastructure-Enablement.html">Site Preparation &amp; Infrastructure Enablement</a></li>
                                            <li><a href="Interior-Design-Fit-out-Finishing.html">Interior Design, Fit-out &amp; Finishing</a></li>
                                        </ul>
                                    </li>
                                    <li class="dropdown"><a href="projects.html">Projects</a>
                                        <ul>
                                           <li><a href="Commercial-projects.html">Commercial</a></li>
                                            <li><a href="Residential-projects.html">Residential</a></li>
                                            <li><a href="Industrial-projects.html">Industrial</a></li>
                                            <li><a href="Hospitality-Projects.html"> Hospitality</a></li>
                                            <li><a href="Reconstruction-projects.html">Reconstruction</a></li>
                                        </ul>
                                    </li>
                                    <li class="current"><a href="blog.html">Blog</a></li>
                                    <li><a href="contact-2.html">Contact</a></li>
                                 </ul>
                            </div>
                        </nav>
                    </div>
                </div>
            </div>
    </div>
    <!--End Sticky Header-->

    <main id="main-content">

    <!-- Page Title -->
    <section class="page-title" style="background-image:url(images/background/12.webp)">
        <div class="auto-container">
            <h1>Blog</h1>
            <ul class="page-breadcrumb">
                <li><a href="index.html">Home</a></li>
                <li>Blog</li>
            </ul>
        </div>
    </section>
    <!-- End Page Title -->

    <!--Blog Page Section-->
    <section class="blog-page-section">
    \t<div class="auto-container">
        \t<div class="inner-container">
                <div id="blog-results-message" class="text-center" role="status" aria-live="polite" hidden></div>
                <div class="row clearfix">

{cards_html}
                </div>
            </div>
        </div>
    </section>
    <!--End Blog Page Section-->

    </main>
    {FOOTER_HTML}

</div>
<!--End pagewrapper-->

<!--Scroll to top-->
<div class="scroll-to-top scroll-to-target" data-target="html"><span class="fa fa-arrow-up"></span></div>

<script src="js/jquery.js"></script>
<script src="js/bootstrap.min.js"></script>
<script src="js/appear.js"></script>
<script src="js/script.js?v=20261016"></script>
<script src="js/blog.js"></script>
<script src="js/social-sharing.js"></script>

</body>
</html>'''
    return blog_html


def _atomic_write(path: Path, content: str):
    """Write content to path atomically using a temp file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    suffix = path.suffix or '.tmp'
    fd, tmp_path = tempfile.mkstemp(suffix=suffix, dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)
        shutil.move(tmp_path, str(path))
    except Exception:
        try:
            os.unlink(tmp_path)
        except Exception:
            pass
        raise


def validate_article(article) -> list:
    """Return list of validation error strings, or empty list if valid."""
    errors = []
    if not article.title or not article.title.strip():
        errors.append('Title is required.')
    if not article.slug or not article.slug.strip():
        errors.append('Slug is required.')
    if not article.content or not article.content.strip():
        errors.append('Content is required.')
    if len(article.slug) > 200:
        errors.append('Slug must be 200 characters or fewer.')
    return errors


def write_article_file(article, html: str):
    """Write article HTML to site root as congo-prime-{slug}.html"""
    output_path = SITE_ROOT / article.html_filename
    _atomic_write(output_path, html)
    return output_path


def update_blog_listing(user=None):
    """
    Regenerate blog.html with all published articles (newest first).
    """
    from apps.articles.models import Article as ArticleModel
    articles = ArticleModel.objects.filter(
        status=ArticleModel.STATUS_PUBLISHED
    ).order_by('-published_at').prefetch_related('categories', 'tags', 'featured_image', 'author')

    html = render_blog_listing_html(articles)
    output_path = SITE_ROOT / 'blog.html'
    _atomic_write(output_path, html)
    return output_path


def update_redirects(article):
    """
    Ensure _redirects contains the clean URL → HTML filename mapping for this article.
    Does NOT remove existing entries.
    """
    redirects_path = SITE_ROOT / '_redirects'
    clean_url = f'/blog/{article.slug}'
    html_file = article.html_filename
    new_line = f'{clean_url} /{html_file} 200'

    content = ''
    if redirects_path.exists():
        content = redirects_path.read_text(encoding='utf-8')

    # Only add if not already present
    if clean_url not in content:
        lines = content.rstrip('\n').split('\n')
        # Find the canonical clean blog URLs section
        insert_idx = None
        for i, line in enumerate(lines):
            if '# Canonical clean blog URLs' in line:
                insert_idx = i + 1
                break

        if insert_idx is not None:
            lines.insert(insert_idx, new_line)
        else:
            lines.insert(0, '# Canonical clean blog URLs')
            lines.insert(1, new_line)

        _atomic_write(redirects_path, '\n'.join(lines) + '\n')


def update_server_routes(article):
    """
    Ensure server.js cleanRoutes contains the route for this article.
    """
    server_path = SITE_ROOT / 'server.js'
    if not server_path.exists():
        return

    content = server_path.read_text(encoding='utf-8')
    slug = article.slug
    html_file = article.html_filename
    route_entry = f"  '/blog/{slug}': '{html_file}',"

    if f"'/blog/{slug}'" not in content:
        # Insert before closing brace of cleanRoutes object
        content = content.replace(
            '};',
            f'{route_entry}\n}};',
            1  # Only first occurrence
        )
        _atomic_write(server_path, content)


def publish_article(article, user) -> dict:
    """
    Full publishing pipeline:
    1. Validate
    2. Render HTML
    3. Write article file
    4. Update blog listing
    5. Update _redirects
    6. Update server.js routes
    7. Record publishing event
    8. Update article status

    Returns: {'success': bool, 'errors': list, 'output_path': str}
    """
    from apps.history.models import PublishingEvent
    from django.utils import timezone

    errors = validate_article(article)
    if errors:
        event = PublishingEvent.objects.create(
            article=article,
            action=PublishingEvent.ACTION_PUBLISH,
            performed_by=user,
            success=False,
            error_message='; '.join(errors)
        )
        return {'success': False, 'errors': errors, 'output_path': None}

    try:
        html = render_article_html(article)
        output_path = write_article_file(article, html)
        update_blog_listing(user)
        update_redirects(article)
        update_server_routes(article)

        # Update article status
        article.status = article.STATUS_PUBLISHED
        if not article.published_at:
            article.published_at = timezone.now()
        article.save(update_fields=['status', 'published_at', 'updated_at'])

        PublishingEvent.objects.create(
            article=article,
            action=PublishingEvent.ACTION_PUBLISH,
            performed_by=user,
            success=True,
            detail=str(output_path)
        )
        return {'success': True, 'errors': [], 'output_path': str(output_path)}

    except Exception as e:
        PublishingEvent.objects.create(
            article=article,
            action=PublishingEvent.ACTION_PUBLISH,
            performed_by=user,
            success=False,
            error_message=str(e)
        )
        return {'success': False, 'errors': [str(e)], 'output_path': None}


def unpublish_article(article, user) -> dict:
    """
    Unpublish: remove generated HTML file, update blog listing, update status.
    """
    from apps.history.models import PublishingEvent

    try:
        # Remove article HTML file
        article_path = SITE_ROOT / article.html_filename
        if article_path.exists():
            article_path.unlink()

        article.status = article.STATUS_UNPUBLISHED
        article.save(update_fields=['status', 'updated_at'])

        update_blog_listing(user)

        PublishingEvent.objects.create(
            article=article,
            action=PublishingEvent.ACTION_UNPUBLISH,
            performed_by=user,
            success=True
        )
        return {'success': True, 'errors': []}

    except Exception as e:
        PublishingEvent.objects.create(
            article=article,
            action=PublishingEvent.ACTION_UNPUBLISH,
            performed_by=user,
            success=False,
            error_message=str(e)
        )
        return {'success': False, 'errors': [str(e)]}

