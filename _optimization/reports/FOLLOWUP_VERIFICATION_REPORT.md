# Follow-up Verification & Fix Report

Date: 2026-10-15 (follow-up to `OPTIMIZATION_REPORT.md` / `feat: WebP migration...` commit `87539f8`)

## Why this exists

The prior migration commit's own `broken_refs_after_fix.json` reported **1274 broken
references** post-migration (668 "still broken", split into 47 "pre-existing" + 147
"new issues" after de-duplication, plus a much larger raw count before
de-duplication). That number blends in ~500+ orphaned/duplicate pages
(`public_html/`, `store/`, and stray demo files like `congo.html`,
`anotherhhhhhhhhhhhhhhhhhhhh.html`, `efefefe.html`, `notrelavent.html`) that are not
part of the live, nav-linked site and were already out of scope by prior agreement
with the user.

This pass re-validated **only the 22 genuine, nav-linked pages** (the ones a real
visitor reaches from the header/footer) plus the 3 CSS files they load
(`style.css`, `responsive.css`, `color.css`), using two purpose-built checkers
(`_optimization/validate_genuine2.py` for `src`/`href`/`data-*`/CSS `url()`, and
`_optimization/validate_inline_style.py` for inline `style="background-image:url(...)"`,
which the first pass's own validator had not covered).

## What was actually broken on the live site

Initial scan: **479 image references** on genuine pages/CSS, of which **278** resolved
to files that did not exist on disk (39 unique missing paths; the count is inflated
because several of these, like the favicon and the footer background, are included
on every page).

Root cause, case by case:

| Issue | Scope | Cause |
|---|---|---|
| `images/favicon-icon.webp` | All 22 pages (tab icon broken everywhere) | HTML `<link>` was rewritten to `.webp` but the file was never converted — only `favicon-icon.png` exists. Favicons should not have been touched. |
| `images/background/6.webp` | Site-wide footer background — all 21 pages that render the footer | Migration deleted `background/6.jpg` without creating `background/6.webp`. |
| `images/background/4.webp` | `index.html` sidebar-news panel | Same pattern as above. |
| `images/projects/{commercial,hospitality,industrial,reconstruction}/*-0{1-5}.webp` (20 files) | The project gallery grid on `projects.html` + 5 category pages | The migration commit (`87539f8`) *did* produce correct `.webp` files for these, but they were missing from the final working tree/branch tip (`a1ce15d`) — recovered intact from the `87539f8` commit tree. |
| `images/projects/residential/villa-3.webp`, `images/resource/image-3.webp`, `images/resource/project-4.webp` | `projects-detail.html`, `about.html` | Same as above — recovered from `87539f8`. |
| `images/gallery/17–21.webp` | `index.html` gallery section | Deleted with no replacement; original `.jpg` recovered from the pre-migration baseline commit (`608b94c`) and freshly converted (quality 82). |
| `images/resource/author-3.webp`, `news-11.webp`, `post-thumb-1..4.webp` | `blog-detail.html` (related-posts widget) | Same as above — recovered + converted fresh. |

**Fix applied:** 23 WebP files restored byte-for-byte from the migration commit's own
tree (they existed there and were simply missing from the final branch state); 13
more (11 image files + the 2 background images above) recovered as JPG originals
from the pre-migration baseline commit and freshly converted to WebP at quality 82.
The favicon `<link>` tags were reverted to `.png` (the file that actually exists)
across all 32 root-level HTML pages, since favicons should stay in their native
format per the original task's own rules.

**3 stray/orphaned files cleaned up:** `images/projects/food-town (1).jpg` (exact
duplicate of an already-quarantined file), `images/projects/food-town.jpg` (loose,
unreferenced — the real one lives at `images/projects/commercial/food-town.webp`),
and `images/test_commercial.jpg` (unreferenced test file) — all quarantined/removed
from the live tree, duplicates matching already-quarantined copies were git-rm'd
rather than double-stored.

**Deployment hole closed:** `.assetsignore` only excluded `.git` — the entire
`_optimization/` directory (32 MB: Python scripts, quarantined originals, audit
reports) would have been publicly served by Cloudflare Pages once pushed. Added
`_optimization/` and `_optimization/**` to `.assetsignore`.

## Remaining known gaps (confirmed pre-existing, not caused by this task, not visibly broken)

Verified via `git log --all` that none of these ever existed at any commit in this
repository's history — they are gaps in the original template/content, not
regressions:

- `images/background/process-bg.jpg` — referenced only by a CSS rule for the
  "Our Process" section in `about.html`, which is currently commented out
  (confirmed by the user earlier in this engagement). Never rendered.
- `images/main-slider/image-10/11/12.{png,jpg}` — these are Revolution Slider
  `data-thumb` attributes (slide-picker thumbnails). The slider's own init config
  (`js/main-slider-script.js`) has no `thumb` navigation enabled, so these
  attributes are never read or requested by the browser (confirmed: zero network
  requests for these paths in live testing).

Neither is visible to a site visitor under any normal interaction.

## Verification performed

- Re-ran both validators after fixes: **0** broken references in genuine scope
  (down from 278), except the 4 pre-existing/inert paths above.
- Live browser check (local static server) on `index.html`, `about.html`,
  `Commercial-projects.html`, `blog-detail.html`, `projects-detail.html`: all
  previously-404ing requests now return 200; zero new console errors (only the
  pre-existing, non-fatal Revolution Slider `"Can not detect viewport width"`
  warning, unrelated to images).
- Confirmed no `<picture>`/`srcset` usage anywhere in genuine pages (nothing missed
  there).
- Confirmed remaining JPG/PNG in `images/` (12 files after cleanup) are all
  legitimate non-photographic assets (favicons, fancybox plugin sprites, small
  UI icons) that should not be WebP.

## Not in scope / untouched (as previously agreed with the user)

- `public_html/` and `store/` — full duplicate copies of the site, not reachable
  from the live nav, left as-is.
- Orphaned demo pages at repo root (`congo.html`, `efefefe.html`,
  `anotherhhhhhhhhhhhhhhhhhhhh.html`, `notrelavent.html`, individual
  `*-project.html` files not linked from `projects.html`).
