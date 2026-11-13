# Schema Implementation Report — Congo Prime Construction
**Date:** 2026-11-13  

---

## Summary

| Schema Type | Pages Implemented | Status |
|------------|------------------|--------|
| GeneralContractor | index.html | ✅ |
| WebSite | index.html | ✅ |
| WebPage | 20+ pages | ✅ |
| BreadcrumbList | 20 inner pages | ✅ |
| Service | 6 service pages | ✅ |
| BlogPosting | 5 blog posts | ✅ |
| ImageObject | 5 blog posts | ✅ |
| LocalBusiness (with address) | None | ❌ Awaiting verified address |
| Product | N/A | — |
| Review / AggregateRating | None | ❌ Not added (no verified reviews) |
| Event | N/A | — |
| JobPosting | N/A | — |

---

## 1. GeneralContractor Schema — `index.html`

```json
{
  "@type": "GeneralContractor",
  "@id": "https://congoprime.com/#organization",
  "name": "Congo Prime Construction SARL",
  "description": "...",
  "areaServed": ["Lubumbashi", "Kolwezi", "Likasi", "Haut-Katanga", "Lualaba", "DRC"],
  "logo": { "@type": "ImageObject", "url": "https://congoprime.com/images/logo-2.webp" },
  "sameAs": ["Instagram", "Facebook", "YouTube"]
}
```

**Notes:**
- Upgraded from plain `Organization` to `GeneralContractor` (more specific for construction companies)
- `areaServed` added for Lubumbashi, Kolwezi, Likasi and DRC
- `address`, `telephone`, `openingHoursSpecification` NOT added — awaiting verified business info from client

---

## 2. WebSite Schema — `index.html`

```json
{
  "@type": "WebSite",
  "@id": "https://congoprime.com/#website",
  "url": "https://congoprime.com/",
  "name": "Congo Prime Construction",
  "publisher": { "@id": "https://congoprime.com/#organization" }
}
```

---

## 3. WebPage Schema — All Main Pages

Present on all indexable pages. Example (about.html):

```json
{
  "@type": "WebPage",
  "name": "About Congo Prime Construction | Lubumbashi, DRC",
  "url": "https://congoprime.com/about.html",
  "description": "...",
  "isPartOf": { "@id": "https://congoprime.com/#website" }
}
```

**Pages with WebPage schema:** index.html (via graph), about.html, services.html, all service pages, all project pages, blog.html, contact-2.html, blog-detail.html, projects-detail.html

---

## 4. BreadcrumbList Schema — 20 Inner Pages

Added to all inner pages (not homepage). Three-level hierarchy for service and project subsection pages.

**Example (Civil-Structural-Works.html):**
```json
{
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://congoprime.com/"},
    {"@type": "ListItem", "position": 2, "name": "Services", "item": "https://congoprime.com/services.html"},
    {"@type": "ListItem", "position": 3, "name": "Civil & Structural Works", "item": "https://congoprime.com/Civil-Structural-Works.html"}
  ]
}
```

---

## 5. Service Schema — 6 Service Pages

```json
{
  "@type": "Service",
  "name": "Civil & Structural Engineering Works",
  "description": "...",
  "url": "https://congoprime.com/Civil-Structural-Works.html",
  "provider": { "@id": "https://congoprime.com/#organization" },
  "areaServed": { "@type": "Country", "name": "Democratic Republic of the Congo" }
}
```

**Service pages:**
1. Project Planning & Development
2. Design & Build / Turnkey Solutions
3. Civil & Structural Works
4. MEP Solutions
5. Interior Design, Fit-out & Finishing
6. Site Preparation & Infrastructure Enablement

---

## 6. BlogPosting Schema — 5 Blog Posts

All 5 blog posts (`congo-prime-*.html`) already had BlogPosting schema. Verified fields present:

| Field | Status |
|-------|--------|
| `@type: BlogPosting` | ✅ |
| `headline` | ✅ |
| `description` | ✅ |
| `url` | ✅ |
| `image` | ✅ |
| `datePublished` | ✅ |
| `dateModified` | ✅ |
| `author` (Organization) | ✅ |
| `publisher` (Organization) | ✅ |
| `article:published_time` OG tag | ✅ |

---

## 7. ImageObject Schema — 5 Blog Posts

Each blog post has an `ImageObject` schema for the featured image, including `url`, `width`, `height`, `caption`.

---

## 8. Schema NOT Implemented (and Why)

| Schema Type | Reason |
|-------------|--------|
| `LocalBusiness` with address | Verified address not available — NEVER add fake/unverified data |
| `AggregateRating` / `Review` | No verified review source — adding fake ratings is a Google policy violation |
| `Event` | No events identified |
| `FAQPage` | No FAQ sections in current content |
| `HowTo` | No how-to content in current pages |
| `Person` schema (team) | No verified team member info available |
| `Product` | Construction services are not products |

---

## 9. Schema Validation Checklist

After deployment, validate using:

1. **Google Rich Results Test:** https://search.google.com/test/rich-results  
   Test: `https://congoprime.com/`  
   Expected: GeneralContractor, WebSite, BreadcrumbList eligible  

2. **Schema.org Validator:** https://validator.schema.org/  
   Paste JSON-LD from each page type  

3. **Google Search Console — Enhancements tab**  
   Check for Breadcrumb and other rich result errors after indexing  

---

*Schema report by Antigravity SEO Agent for Congo Prime Construction SARL*

