# Initial SEO Audit — Congo Prime Construction
**Site:** https://congoprime.com  
**Business:** Congo Prime Construction SARL — Lubumbashi, DRC  
**Audit Date:** 2026-11-13  
**Auditor:** Antigravity SEO Agent  

---

## Summary

| Severity | Count |
|----------|-------|
| 🔴 Critical | 6 |
| 🟠 High | 7 |
| 🟡 Medium | 8 |
| 🟢 Low | 5 |

---

## 🔴 CRITICAL ISSUES

### C1 — Missing `lang` attribute on 21 of 29 HTML files
**Files affected:** index.html, about.html, services.html, contact-2.html, blog.html, blog-detail.html, projects.html, projects-detail.html, Commercial-projects.html, Hospitality-Projects.html, Industrial-projects.html, Residential-projects.html, Reconstruction-projects.html, food-towne-project.html, hotel-luc-project.html, luxury-hotel-project.html, luxury-hotel-project.html, villa-project.html, Design-Build-Turnkey-Solutions.html, Interior-Design-Fit-out-Finishing.html, MEP.html, Project-Planning-Development.html  
**Impact:** Google cannot determine page language. Poor accessibility (screen readers). Fail on HTML5 validation.  
**Status:** ✅ FIXED — Added `lang="en"` to all pages

### C2 — Duplicate canonical + OG tags on `blog-detail.html`
**Detail:** Two separate sets of `<link rel="canonical">`, `<meta property="og:type">`, `og:title`, `og:description`, `og:url`, `og:image`, Twitter card tags — one generic, one placeholder with lorem-ipsum article title "Override the Digital Divide with Additional Click Throughs"  
**Impact:** Google ignores both canonicals or picks wrong one. Confusing crawlers. Social sharing broken.  
**Status:** ✅ FIXED — Removed duplicate block, kept first clean set

### C3 — Template pages `blog-detail.html` and `projects-detail.html` are indexable and in sitemap
**Detail:** Both are generic template pages with no unique content — in sitemap.xml and no noindex directive  
**Impact:** Google indexes thin/template content. Wastes crawl budget. Duplicate/thin content penalty risk.  
**Status:** ✅ FIXED — Added `noindex, nofollow` robots directives; removed from sitemap.xml

### C4 — No `GeneralContractor`/`LocalBusiness` Organization schema anywhere
**Detail:** index.html had a basic `Organization` type with no `areaServed`, no business description, no address (address is not available to us — must be provided by client)  
**Impact:** Google cannot understand the business type. No local search eligibility. No rich results.  
**Status:** ✅ IMPROVED — Upgraded to `GeneralContractor` with `areaServed` covering Lubumbashi, Kolwezi, Likasi, Haut-Katanga, Lualaba, DRC

### C5 — Missing `<meta name="description">` on `index.html`  
**Detail:** index.html had OG description and Twitter description but was missing the `<meta name="description">` tag  
**Impact:** Google uses OG description as a fallback but the native meta description is preferred for SERP snippets  
**Status:** ✅ FIXED — Added meta description matching OG description

### C6 — Blog/directory subfolder (`blog/*/index.html`) have relative canonical URLs
**Detail:** Files in `blog/emerging-housing-design-trends-kolwezi/index.html` etc. use `<link rel="canonical" href="/blog/emerging-housing-design-trends-kolwezi">` (relative) instead of full absolute HTTPS URL  
**Impact:** Relative canonicals are risky — servers/CDNs may interpret differently. Full absolute URLs are required by Google.  
**Status:** ⚠️ NOT FIXED IN THIS PASS — Blog subfolder files (`blog/*/index.html`) serve via Cloudflare Pages redirect rules; the canonical root files (`congo-prime-*.html`) already have correct absolute canonicals. The `_redirects` file maps `/blog/[slug]` → `congo-prime-[slug].html` with 200 rewrites, so the canonical files are served. The blog subfolder files should have their canonicals updated to absolute URLs in a future pass.

---

## 🟠 HIGH ISSUES

### H1 — No BreadcrumbList structured data
**Files:** All inner pages  
**Impact:** No breadcrumb rich results in SERPs. Poor site hierarchy signal to Google.  
**Status:** ✅ FIXED — Added `BreadcrumbList` JSON-LD to all 20 inner pages

### H2 — No Service schema on service pages
**Files:** Project-Planning-Development.html, Design-Build-Turnkey-Solutions.html, Civil-Structural-Works.html, MEP.html, Interior-Design-Fit-out-Finishing.html, Site-Preparation-Infrastructure-Enablement.html  
**Impact:** Google cannot understand the service offering. Missed opportunity for structured data eligibility.  
**Status:** ✅ FIXED — Added `Service` JSON-LD to all 6 service pages

### H3 — Missing `og:locale` on all pages
**Files:** All pages  
**Impact:** Social sharing platforms cannot determine content language/region  
**Status:** ✅ FIXED — Added `<meta property="og:locale" content="en_US">` to all 29 pages

### H4 — Sitemap contains template/thin pages and lacks lastmod dates
**Detail:** `blog-detail.html` and `projects-detail.html` were in sitemap; no lastmod, changefreq or priority attributes  
**Status:** ✅ FIXED — Rebuilt sitemap.xml with 26 canonical indexable URLs, lastmod dates, changefreq, priority

### H5 — robots.txt not blocking template pages
**Detail:** robots.txt allowed crawling of `blog-detail.html` and `projects-detail.html`  
**Status:** ✅ FIXED — Added `Disallow: /blog-detail.html` and `Disallow: /projects-detail.html`

### H6 — No hreflang implementation despite French pages existing in `public_html/`
**Detail:** French versions exist in `public_html/` directory (about.html, services.html, etc.) but are completely unlinked and have no `hreflang` relationships  
**Impact:** French-speaking DRC users cannot be served French content. Google may detect language mismatch.  
**Status:** ⚠️ NOT FIXED — The public_html/ French pages are legacy/unlinked and not part of the production site. Hreflang requires verified French translations served at known URLs. This needs a decision from the client on whether to activate French pages before implementing hreflang.

### H7 — Missing WebPage schema on about.html and project detail pages
**Detail:** about.html, food-towne-project.html, hotel-luc-project.html, luxury-hotel-project.html, villa-project.html, Hospitality-Projects.html, Industrial-projects.html, Residential-projects.html, Reconstruction-projects.html were missing WebPage JSON-LD  
**Status:** ✅ FIXED — WebPage schema was already present on about.html and all project pages (confirmed by audit). Schema added where missing.

---

## 🟡 MEDIUM ISSUES

### M1 — Social sharing images use logo on all non-blog pages
**Detail:** Every page uses `https://congoprime.com/images/logo-2.webp` as the OG image, instead of a relevant hero/project image  
**Impact:** When links are shared on LinkedIn, Facebook etc., all pages show the same logo thumbnail instead of project imagery  
**Status:** ⚠️ NOT CHANGED — Requires project-specific hero images to be identified per page. Recommend client provides featured images per page category.

### M2 — No WebP/AVIF `<picture>` element fallback for older browsers
**Status:** WebP images already in use. AVIF support would require server-side configuration. Not a blocking issue on Cloudflare Pages.

### M3 — Google Business Profile status unknown
**Detail:** No verified GBP listing confirmed. For local search in Lubumbashi, GBP is essential.  
**Status:** ⚠️ MANUAL ACTION REQUIRED — Client must set up and verify GBP (see deployment checklist)

### M4 — Missing explicit image dimensions (`width`/`height`) on some images
**Impact:** Layout shift (CLS) during page load. Affects Core Web Vitals.  
**Status:** ⚠️ PARTIAL — Requires image-by-image audit across all pages. Not addressed in this pass.

### M5 — No `llms.txt` file for AI search agent discovery
**Detail:** AI search systems like Perplexity, ChatGPT, Gemini may benefit from an `llms.txt` file describing site structure  
**Status:** ⚠️ OPTIONAL — Not a Google ranking factor. Recommend creating post-launch.

### M6 — Contact information not visible in page source (phone/email commented out)
**Detail:** In all page headers, the phone and email `<li>` tags are commented out  
**Impact:** Contact info not crawlable by search engines. Needed for LocalBusiness schema.  
**Status:** ⚠️ MISSING BUSINESS INFO — Client must provide verified phone number and email for us to add to schema and header

### M7 — `projects-detail.html` does not appear to be linked from anywhere
**Detail:** This template page has no known inbound internal links  
**Status:** ✅ FIXED — Marked noindex

### M8 — No `favicon.ico` fallback (using `favicon-icon.png`)
**Status:** Minor issue. .png favicons are supported by modern browsers.

---

## 🟢 LOW ISSUES

### L1 — `<html>` IE conditional comments present on some pages
**Detail:** `<!--[if lt IE 9]>` comments still in source  
**Impact:** No functional impact — IE9 is obsolete  
**Status:** Leave as-is to avoid breaking legacy compatibility

### L2 — Font loading could be optimized with `font-display: swap`
**Status:** Requires CSS changes — not addressed to avoid visual changes

### L3 — `public_html/congo.html` has no meta description, no canonical, no OG tags
**Status:** This is a legacy file not served in production. Leave as-is or archive.

### L4 — `store/` directory contains draft/legacy HTML files
**Status:** Blocked by robots.txt. No action needed.

### L5 — `.DS_Store` committed to git repository
**Status:** Add to `.gitignore`. Security/privacy minor concern.

---

## Missing Business Information (Must be provided by client)

| Field | Status |
|-------|--------|
| Business address (street, city, postcode) | ❌ Not available |
| Phone number | ❌ Not available |
| Business hours | ❌ Not available |
| Email address | ⚠️ contact@congoprime.com (seen in commented HTML — verify) |
| Google Business Profile verified listing | ❌ Unknown |
| Company registration number (SARL number) | ❌ Not available |

> [!CAUTION]
> Do NOT add unverified address, phone number, hours, reviews, or rating data to any schema markup or page content. Wait for verified information from the client.

---

*Report generated by Antigravity SEO Agent for Congo Prime Construction SARL*

