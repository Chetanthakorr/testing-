# Technical SEO Changes Log — Congo Prime Construction
**Date:** 2026-11-13  

---

## Summary of Changes

| Category | Changes Made | Files Affected |
|----------|-------------|----------------|
| HTML `lang` attribute | Added `lang="en"` | 21 HTML files |
| Meta robots noindex | Added to template pages | 2 files |
| Duplicate tag removal | Removed duplicate OG/canonical block | 1 file (blog-detail.html) |
| og:locale | Added `og:locale` | 29 files |
| Organization schema | Upgraded to GeneralContractor | index.html |
| BreadcrumbList schema | Added to all inner pages | 20 files |
| Service schema | Added to service pages | 6 files |
| Sitemap.xml | Rebuilt with correct URLs + dates | sitemap.xml |
| robots.txt | Added disallow for template pages | robots.txt |

---

## Detailed Changes

### 1. `lang="en"` Added to `<html>` Tag

**Files changed:**
- about.html
- blog.html
- blog-detail.html
- contact-2.html
- Commercial-projects.html
- Design-Build-Turnkey-Solutions.html
- food-towne-project.html
- Hospitality-Projects.html
- hotel-luc-project.html
- index.html
- Industrial-projects.html
- Interior-Design-Fit-out-Finishing.html
- luxury-hotel-project.html
- MEP.html
- Project-Planning-Development.html
- projects-detail.html
- projects.html
- Reconstruction-projects.html
- Residential-projects.html
- services.html
- villa-project.html

**Change:** `<html>` → `<html lang="en">`

---

### 2. `blog-detail.html` — Duplicate Tags Removed

**Removed:** Lines 18–31 of original (second canonical + second OG/Twitter block containing "Override the Digital Divide…" placeholder content)

**Added:** `<meta name="robots" content="noindex, nofollow">` after canonical tag

---

### 3. `projects-detail.html` — Noindex Added

**Added:** `<meta name="robots" content="noindex, nofollow">` after canonical tag

---

### 4. `og:locale` Added to All Pages (29 files)

**Tag added:** `<meta property="og:locale" content="en_US">`  
**Insertion point:** After `<meta property="og:site_name" content="Congo Prime Construction">`

All 29 root HTML files plus 5 blog detail files received this tag.

---

### 5. `index.html` — Organization Schema Upgraded

**Before:** `@type: "Organization"` with no `areaServed`, no business description  
**After:** `@type: "GeneralContractor"` with:
- `areaServed`: Lubumbashi, Kolwezi, Likasi, Haut-Katanga, Lualaba, DRC
- Descriptive `description` field
- `logo` as `ImageObject`
- Social `sameAs` links preserved (Instagram, Facebook, YouTube)

---

### 6. BreadcrumbList Schema Added (20 inner pages)

**Schema type:** `BreadcrumbList` with `ListItem` for each breadcrumb level  
**Inserted:** Before `</head>` on each page

| Page | Breadcrumb Path |
|------|----------------|
| about.html | Home > About Us |
| services.html | Home > Services |
| projects.html | Home > Projects |
| blog.html | Home > Blog |
| contact-2.html | Home > Contact |
| Project-Planning-Development.html | Home > Services > Project Planning & Development |
| Design-Build-Turnkey-Solutions.html | Home > Services > Design & Build / Turnkey Solutions |
| Civil-Structural-Works.html | Home > Services > Civil & Structural Works |
| MEP.html | Home > Services > MEP Solutions |
| Interior-Design-Fit-out-Finishing.html | Home > Services > Interior Design, Fit-out & Finishing |
| Site-Preparation-Infrastructure-Enablement.html | Home > Services > Site Preparation & Infrastructure Enablement |
| Commercial-projects.html | Home > Projects > Commercial Projects |
| Hospitality-Projects.html | Home > Projects > Hospitality Projects |
| Industrial-projects.html | Home > Projects > Industrial Projects |
| Residential-projects.html | Home > Projects > Residential Projects |
| Reconstruction-projects.html | Home > Projects > Reconstruction Projects |
| food-towne-project.html | Home > Projects > Food Towne Project |
| hotel-luc-project.html | Home > Projects > Hotel LUC Project |
| luxury-hotel-project.html | Home > Projects > Luxury Motel Project |
| villa-project.html | Home > Projects > Residential Villa Project |

---

### 7. Service Schema Added (6 service pages)

**Schema type:** `Service` with `name`, `description`, `url`, `provider` (linked to Organization), `areaServed`

| Page | Service Name |
|------|-------------|
| Project-Planning-Development.html | Construction Project Planning & Development |
| Design-Build-Turnkey-Solutions.html | Design & Build / Turnkey Construction Solutions |
| Civil-Structural-Works.html | Civil & Structural Engineering Works |
| MEP.html | MEP (Mechanical, Electrical & Plumbing) Solutions |
| Interior-Design-Fit-out-Finishing.html | Interior Design, Fit-out & Finishing |
| Site-Preparation-Infrastructure-Enablement.html | Site Preparation & Infrastructure Enablement |

---

### 8. `sitemap.xml` — Rebuilt

**Removed entries:**
- `https://congoprime.com/blog-detail.html` (template page)
- `https://congoprime.com/projects-detail.html` (template page)

**Added:**
- `<lastmod>` dates for all URLs
- `<changefreq>` values per URL type
- `<priority>` values (1.0 homepage, 0.9 services, 0.8 key pages, 0.7 blog/projects, 0.6 project details)

**Total URLs in sitemap:** 26

---

### 9. `robots.txt` — Updated

**Added:**
```
Disallow: /blog-detail.html
Disallow: /projects-detail.html
```

---

## Changes NOT Made (and Why)

| Change | Reason Not Made |
|--------|----------------|
| Hreflang tags | French pages in public_html/ are legacy/unlinked — no production French URLs confirmed |
| OG image updates | Requires client-provided project-specific hero images |
| Contact info in header | Verified phone/email not available from client |
| LocalBusiness address schema | Verified address not available from client |
| blog/ subfolder canonical fix | Cloudflare rewrites serve congo-prime-*.html which have correct canonicals |
| `llms.txt` | Optional — not a ranking factor |
| Image dimension attributes | Requires page-by-page image audit |
| Font display optimization | Requires CSS changes — out of scope to avoid visual changes |

---

*Log maintained by Antigravity SEO Agent*

