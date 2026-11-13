# Blog SEO Report — Congo Prime Construction
**Date:** 2026-11-13  

---

## Blog Structure Overview

| URL Type | Files | Status |
|----------|-------|--------|
| Clean URL via `_redirects` | `/blog/[slug]` → `congo-prime-[slug].html` | ✅ Canonical production URLs |
| Root blog files | `congo-prime-*.html` | ✅ Canonical files |
| Subfolder files | `blog/*/index.html` | ⚠️ Relative canonicals (see notes) |
| Blog listing | `blog.html` | ✅ |
| Blog template | `blog-detail.html` | ✅ Noindex applied |

---

## Blog Posts Audited

### Blog 1: Emerging Housing Design Trends in Kolwezi

| Element | Value | Status |
|---------|-------|--------|
| Canonical URL | `https://congoprime.com/blog/emerging-housing-design-trends-kolwezi` | ✅ |
| Title | Emerging Housing Design Trends in Kolwezi \| Congo Prime Construction | ✅ |
| Meta Description | Explore emerging housing design trends in Kolwezi, DRC, including villas, multi-unit developments, security-conscious planning, practical interiors and utility resilience. | ✅ |
| OG Image | `https://congoprime.com/images/blog/blog-2lubumbashi.webp` | ✅ |
| OG Image Alt | Modern residential architecture and housing design trends in Kolwezi | ✅ |
| Schema: BlogPosting | ✅ | |
| Schema: BreadcrumbList | ✅ (Home > Blog > Article) | |
| datePublished | 2025-03-15 | ✅ |
| dateModified | 2025-03-15 | ✅ |
| article:published_time | 2025-03-15T00:00:00+02:00 | ✅ |
| og:locale | en_US | ✅ |
| lang attribute | en | ✅ |
| H1 | ✅ Present | |
| Internal Links | Service pages linked | ✅ |

---

### Blog 2: Construction and Infrastructure Development in Lubumbashi

| Element | Value | Status |
|---------|-------|--------|
| Canonical URL | `https://congoprime.com/blog/construction-and-infrastructure-development-lubumbashi` | ✅ |
| Title | Construction and Infrastructure Development in Lubumbashi | ✅ |
| datePublished | 2025-02-10 | ✅ |
| Schema types | BlogPosting, BreadcrumbList, ImageObject, WebPage | ✅ |
| og:locale | en_US | ✅ |

---

### Blog 3: 10 Points to Keep in Mind While Designing Your Home Interior

| Element | Value | Status |
|---------|-------|--------|
| Canonical URL | `https://congoprime.com/blog/10-points-designing-home-interior` | ✅ |
| Title | 10 Points to Keep in Mind While Designing Your Home Interior | ✅ |
| datePublished | 2025-04-20 | ✅ |
| Schema types | BlogPosting, BreadcrumbList, ImageObject, WebPage | ✅ |
| og:locale | en_US | ✅ |

---

### Blog 4: Building on Solid Ground — Land Acquisition and Permits in Haut-Katanga

| Element | Value | Status |
|---------|-------|--------|
| Canonical URL | `https://congoprime.com/blog/building-solid-ground-land-acquisition-permits-haut-katanga` | ✅ |
| Title | Building on Solid Ground: Land Acquisition and Permits in Haut-Katanga | ✅ |
| datePublished | 2025-05-05 | ✅ |
| Schema types | BlogPosting, BreadcrumbList, ImageObject, WebPage | ✅ |

---

### Blog 5: Engineering Katanga Homes to Defeat the Wet Season

| Element | Value | Status |
|---------|-------|--------|
| Canonical URL | `https://congoprime.com/blog/engineering-katanga-homes-defeat-wet-season` | ✅ |
| Title | Engineering Katanga Homes to Defeat the Wet Season | ✅ |
| datePublished | 2025-06-12 | ✅ |
| Schema types | BlogPosting, BreadcrumbList, ImageObject, WebPage | ✅ |

---

## ⚠️ Known Issue: Blog Subfolder Relative Canonicals

The files at `blog/*/index.html` (e.g., `blog/emerging-housing-design-trends-kolwezi/index.html`) use **relative** canonical URLs:

```html
<link rel="canonical" href="/blog/emerging-housing-design-trends-kolwezi">
```

**Should be:**
```html
<link rel="canonical" href="https://congoprime.com/blog/emerging-housing-design-trends-kolwezi">
```

**Risk:** Relative canonicals can be misinterpreted. However, since Cloudflare Pages rewrites `/blog/[slug]` to serve `congo-prime-[slug].html` (which has correct absolute canonicals), and the blog subfolder files do not appear in the sitemap, the risk is **low** in practice.

**Recommendation:** Update the subfolder files to use absolute canonical URLs in a future maintenance pass.

---

## Blog Content Quality Notes

| Blog | Content Quality | Accuracy |
|------|----------------|---------|
| Housing Trends Kolwezi | Good — specific to Kolwezi housing market | ✅ No fabricated data found |
| Infrastructure Lubumbashi | Good — covers DRC construction growth | ✅ No fabricated data found |
| Home Interior Tips | Good — practical 10-point guide | ✅ No fabricated data found |
| Land Acquisition Haut-Katanga | Good — covers permit process | ✅ No legal guarantees fabricated |
| Wet Season Engineering | Good — practical engineering advice | ✅ No engineering guarantees fabricated |

---

## Internal Linking Opportunities (Blog → Service/Project Pages)

| Blog | Recommended Internal Links |
|------|--------------------------|
| Housing Trends Kolwezi | → Residential-projects.html, Interior-Design-Fit-out-Finishing.html |
| Infrastructure Lubumbashi | → Civil-Structural-Works.html, Site-Preparation-Infrastructure-Enablement.html |
| Home Interior Tips | → Interior-Design-Fit-out-Finishing.html |
| Land Acquisition | → Project-Planning-Development.html, contact-2.html |
| Wet Season Engineering | → Civil-Structural-Works.html, Site-Preparation-Infrastructure-Enablement.html |

---

## Future Blog Post Recommendations

| Topic | Target Keyword | Intent |
|-------|---------------|--------|
| Construction Permits Process DRC | building permit DRC | Informational |
| MEP Design for Commercial Buildings | MEP design DRC | Informational |
| Choosing a Construction Contractor in Lubumbashi | hire contractor Lubumbashi | Commercial |
| Mining Camp Construction in Lualaba | mining construction Lualaba | Commercial |
| Industrial Warehouse Construction DRC | warehouse construction DRC | Commercial |
| Renovation vs Reconstruction DRC | building renovation DRC | Informational |

---

*Blog SEO report by Antigravity SEO Agent for Congo Prime Construction SARL*

