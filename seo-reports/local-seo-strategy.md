# Local SEO Strategy — Congo Prime Construction SARL
**Market:** Democratic Republic of the Congo (DRC)  
**Primary City:** Lubumbashi, Haut-Katanga  
**Date:** 2026-11-13  

---

## Target Locations

| Location | Province | Priority | Use Case |
|----------|----------|----------|----------|
| Lubumbashi | Haut-Katanga | ⭐⭐⭐ Primary | Homepage, all service pages, contact |
| Kolwezi | Lualaba | ⭐⭐ High | Blog (housing trends), services |
| Likasi | Haut-Katanga | ⭐⭐ High | Hotel LUC project page |
| Haut-Katanga | Province | ⭐⭐ High | Homepage, about, blog |
| Lualaba | Province | ⭐ Medium | Homepage, about |

---

## 1. Google Business Profile (GBP) — PRIORITY ACTION

> [!IMPORTANT]
> Setting up and verifying a Google Business Profile is the single highest-impact local SEO action for Congo Prime. It directly affects the Local Pack (map results) for searches like "construction company Lubumbashi".

### Steps Required (Manual — Client Action)

1. Go to https://business.google.com and sign in with a business Google account
2. Search for "Congo Prime Construction" to see if a listing already exists
3. If it exists: **Claim and verify** the listing
4. If not: **Create a new listing** with:
   - Business name: **Congo Prime Construction SARL** (consistent name)
   - Category: **General Contractor** (primary), Construction Company (secondary)
   - Address: *[Provide verified physical office address in Lubumbashi]*
   - Phone: *[Provide verified business phone number]*
   - Website: https://congoprime.com
   - Hours: *[Provide verified business hours]*
   - Description: Professional construction, civil engineering, design-build and infrastructure solutions serving Lubumbashi, Haut-Katanga, Kolwezi and the DRC.
5. **Verify** the listing by postcard, phone or email
6. **Add photos**: office, completed projects, team photos, logo
7. **Add services** matching the website service pages

> [!CAUTION]
> Do not create multiple GBP listings for the same business. Do not use a home address or unverified address.

---

## 2. Business Information Required from Client

The following information is needed before full local schema implementation:

| Field | Status | Notes |
|-------|--------|-------|
| Physical business address | ❌ **NEEDED** | Full street address, Lubumbashi |
| Business phone number | ❌ **NEEDED** | Verified operational number |
| Business email | ⚠️ Likely `contact@congoprime.com` | Confirm with client |
| Business hours | ❌ **NEEDED** | Opening/closing times, days |
| GBP listing URL | ❌ **NEEDED** | After verification |
| Company registration number | ❌ Optional | SARL registration DRC |

---

## 3. LocalBusiness Schema — Ready to Add (Once Verified Info Available)

Add the following to `index.html` once address and phone are confirmed:

```json
{
  "@context": "https://schema.org",
  "@type": "GeneralContractor",
  "@id": "https://congoprime.com/#organization",
  "name": "Congo Prime Construction SARL",
  "url": "https://congoprime.com/",
  "telephone": "+243-XXX-XXX-XXXX",
  "email": "contact@congoprime.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[VERIFIED STREET ADDRESS]",
    "addressLocality": "Lubumbashi",
    "addressRegion": "Haut-Katanga",
    "addressCountry": "CD"
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
      "opens": "08:00",
      "closes": "17:00"
    }
  ],
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": -11.6639,
    "longitude": 27.4794
  }
}
```

> [!CAUTION]
> Do NOT add this until all values are verified. Fake addresses, phone numbers or hours are a GBP policy violation and can result in listing suspension.

---

## 4. NAP Consistency (Name, Address, Phone)

The business name must be consistent everywhere:

- **Correct:** Congo Prime Construction SARL
- **Acceptable short form:** Congo Prime Construction
- Do NOT use: Congo Prime, CPC, Congo Prime SARL (without "Construction")

Apply consistently to:
- Google Business Profile
- Website header / footer
- Schema markup
- Directory citations (if any)
- Social media profiles

---

## 5. Social Media Profiles — Current Status

| Platform | URL | Status |
|----------|-----|--------|
| Instagram | https://www.instagram.com/congoprimeconstructionsarl/ | ✅ Linked |
| Facebook | https://www.facebook.com/profile.php?id=61595428409081 | ✅ Linked |
| YouTube | https://www.youtube.com/@CongoPrimeConstructionSARL | ✅ Linked |
| LinkedIn | `href="#"` (placeholder) | ❌ No URL — fix or remove |

**Action:** Either add a real LinkedIn company page URL or remove the LinkedIn link from navigation.

---

## 6. Location-Specific Content Strategy

### Current pages with location signals
| Page | Location Signals |
|------|-----------------|
| Homepage | Lubumbashi, DRC, Congo (in title, meta, body) |
| Blog: Housing Trends | Kolwezi (in title, body) |
| Blog: Infrastructure | Lubumbashi (in title, body) |
| Blog: Land Acquisition | Haut-Katanga (in title, body) |
| Blog: Wet Season | Katanga (in title, body) |
| Hotel LUC Project | Likasi (in title) |

### Recommended Future Content (Location Pages / Blog Posts)

| Suggested Content | Target Location | Target Keyword |
|------------------|----------------|----------------|
| "Construction Services in Kolwezi" | Kolwezi | construction company Kolwezi |
| "Building Infrastructure in Haut-Katanga" | Haut-Katanga | construction Haut-Katanga |
| "MEP Services for Mining Operations in Lualaba" | Lualaba | MEP services Lualaba |
| "Office Fit-out Services in Lubumbashi" | Lubumbashi | office fit-out Lubumbashi |

> [!NOTE]
> Do not create thin duplicate location pages. Each location page must have unique, valuable content specific to that location. Only create them if you can provide genuinely useful local information.

---

## 7. Local Citations & Directories

Consider listing the business on:

| Directory | Notes |
|-----------|-------|
| Google Business Profile | Priority #1 |
| Facebook Business Page | Already active |
| LinkedIn Company Page | Recommended |
| Bing Places | Secondary |
| Apple Maps | Secondary |
| Kompass Africa | Business directory covering DRC |
| Yellows Africa | African business directory |
| Cylex Africa | Business listings Africa |

---

## 8. Map Integration

The contact page (`contact-2.html`) should include an embedded Google Map once the GBP listing is verified and the address is confirmed. This requires the client to provide the verified address.

Do not embed a map pointing to a generic/incorrect location.

---

*Local SEO strategy by Antigravity SEO Agent for Congo Prime Construction SARL*

