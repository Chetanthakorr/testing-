# Deployment Checklist — Congo Prime Construction SEO
**Date:** 2026-11-13  

> This checklist must be completed before and after deploying to congoprime.com. Work through each section in order.

---

## Phase 1: Pre-Deployment Validation (Local)

### HTML Validation
- [ ] Open VS Code Live Server on `index.html` — verify design unchanged
- [ ] Check `about.html` — verify design unchanged
- [ ] Check `services.html` and all 6 service pages — verify design unchanged
- [ ] Check `projects.html` and all project category pages — verify design unchanged
- [ ] Check `blog.html` — verify design unchanged
- [ ] Check `contact-2.html` — verify design unchanged
- [ ] Check all 5 blog posts (`congo-prime-*.html`) — verify design unchanged
- [ ] Verify `blog-detail.html` loads but is NOT linked from navigation
- [ ] Verify `projects-detail.html` loads but is NOT linked from navigation
- [ ] Test mobile layout on each key page (Chrome DevTools → mobile viewport)

### Schema Validation
- [ ] Copy JSON-LD from `index.html` → paste into https://validator.schema.org — expect no errors
- [ ] Copy JSON-LD from `about.html` → validate — expect WebPage + BreadcrumbList
- [ ] Copy JSON-LD from `Civil-Structural-Works.html` → validate — expect WebPage + BreadcrumbList + Service
- [ ] Copy JSON-LD from `congo-prime-emerging-housing-design-trends-kolwezi.html` → validate — expect BlogPosting + BreadcrumbList
- [ ] Test with Google Rich Results Test: https://search.google.com/test/rich-results (requires internet access)

### Meta Tags Verification
- [ ] `index.html` has `<html lang="en">` ✓
- [ ] `index.html` has `<meta name="description">` ✓
- [ ] `index.html` has `<meta property="og:locale" content="en_US">` ✓
- [ ] `blog-detail.html` has `<meta name="robots" content="noindex, nofollow">` ✓
- [ ] `projects-detail.html` has `<meta name="robots" content="noindex, nofollow">` ✓
- [ ] `404.html` has `<meta name="robots" content="noindex, nofollow">` ✓
- [ ] All pages have one (and only one) `<link rel="canonical">` tag

### Sitemap Validation
- [ ] Open `sitemap.xml` — verify 26 URLs present
- [ ] Confirm `blog-detail.html` is NOT in sitemap
- [ ] Confirm `projects-detail.html` is NOT in sitemap
- [ ] Confirm all blog URLs use `/blog/[slug]` clean format
- [ ] Validate XML at: https://www.xml-sitemaps.com/validate-xml-sitemap.html (requires internet)

### Robots.txt Validation
- [ ] Open `robots.txt` — verify contains:
  - `Disallow: /public_html/`
  - `Disallow: /store/`
  - `Disallow: /_optimization/`
  - `Disallow: /.git/`
  - `Disallow: /blog-detail.html`
  - `Disallow: /projects-detail.html`
  - `Sitemap: https://congoprime.com/sitemap.xml`

### Internal Links
- [ ] All navigation links work correctly on all pages
- [ ] Blog listing links point to `/blog/[slug]` clean URLs (not `congo-prime-*.html`)
- [ ] Project category pages link to individual project detail pages
- [ ] Social media links in header work (Instagram, Facebook, YouTube)
- [ ] LinkedIn link either has real URL or is removed

### JavaScript Functionality
- [ ] Project filter buttons work on `projects.html`
- [ ] Blog search/filter works on `blog.html`
- [ ] Language switcher works (if active)
- [ ] Contact form sends correctly on `contact-2.html`
- [ ] Slider/carousel works on `index.html`
- [ ] Mobile hamburger menu works on all pages
- [ ] Image lightbox/fancybox works on project pages

---

## Phase 2: Post-Deployment Verification (Live Site)

### DNS & HTTPS
- [ ] `https://congoprime.com/` loads correctly (HTTPS, not HTTP)
- [ ] `http://congoprime.com/` redirects to HTTPS version
- [ ] `https://www.congoprime.com/` redirects to `https://congoprime.com/` (no www)
- [ ] SSL certificate is valid and not expiring soon

### Sitemap & Robots on Live Site
- [ ] `https://congoprime.com/sitemap.xml` returns 200 OK
- [ ] `https://congoprime.com/robots.txt` returns 200 OK
- [ ] Confirm sitemap accessible via browser
- [ ] Confirm robots.txt accessible via browser

### Social Sharing Preview
- [ ] Test homepage share: https://developers.facebook.com/tools/debug/ — enter `https://congoprime.com/`
- [ ] Test blog post share — enter a blog URL — expect article title + featured image (not logo)
- [ ] Test LinkedIn share preview: https://www.linkedin.com/post-inspector/

---

## Phase 3: Google Search Console (GSC) — Manual Steps

> [!IMPORTANT]
> These steps MUST be completed manually by the site owner.

1. **Add Property**
   - Go to https://search.google.com/search-console/
   - Add `https://congoprime.com/` as a property
   - Verify ownership (HTML file method or DNS record)

2. **Submit Sitemap**
   - In GSC → Sitemaps → Add new sitemap
   - Enter: `https://congoprime.com/sitemap.xml`
   - Submit

3. **Request Indexing for Key Pages**
   - Use URL Inspection tool → enter each key URL → Request Indexing
   - Priority: homepage, services.html, all 6 service pages, projects.html, blog.html, contact-2.html

4. **Monitor Coverage Report**
   - After 1–2 weeks: check Coverage → Excluded pages
   - Confirm `blog-detail.html` and `projects-detail.html` show as "Excluded by robots tag"
   - Confirm all 26 sitemap URLs are indexed or submitted

5. **Check Core Web Vitals**
   - GSC → Core Web Vitals → review LCP, CLS, INP scores
   - Address any "Poor" or "Needs improvement" pages

6. **Monitor Rich Results**
   - GSC → Enhancements → Breadcrumbs
   - After indexing: confirm breadcrumb rich results appearing for inner pages

---

## Phase 4: Google Business Profile (GBP) — Manual Steps

> [!IMPORTANT]
> Requires verified business address, phone, hours from client first.

1. Go to https://business.google.com
2. Search for "Congo Prime Construction" — claim if exists, create if not
3. Set business category: **General Contractor**
4. Add verified address, phone, hours, website URL
5. Add business photos (minimum 5 quality photos):
   - Logo
   - Office exterior
   - Completed project photos (2–3)
   - Team photo (optional)
6. Write a business description (max 750 chars)
7. Add services matching website service pages
8. Verify listing by postcard or phone
9. After verification: add GBP listing URL to `sameAs` array in schema on `index.html`

---

## Phase 5: Ongoing Monitoring

| Task | Frequency |
|------|-----------|
| Check GSC Coverage for new errors | Weekly |
| Review GSC Performance (clicks, impressions) | Weekly |
| Monitor Core Web Vitals | Monthly |
| Check for broken links | Monthly |
| Update sitemap lastmod dates when content changes | As needed |
| Respond to GBP reviews | As they arrive |
| Publish new blog post | Monthly (recommended) |
| Update schema if business info changes | As needed |

---

## ⚠️ Missing Information — Required from Client Before Full Deployment

| Item | Needed For |
|------|-----------|
| Verified business address | LocalBusiness schema, GBP, Contact page |
| Business phone number | LocalBusiness schema, GBP, header |
| Business hours | LocalBusiness schema, GBP |
| Confirmed email address | Schema, Contact page |
| LinkedIn company page URL | Navigation link (currently placeholder `#`) |
| GBP listing URL (after verification) | sameAs in schema |
| Verified publish dates for blog posts | Currently estimated — confirm actual dates |

---

*Checklist prepared by Antigravity SEO Agent for Congo Prime Construction SARL*

