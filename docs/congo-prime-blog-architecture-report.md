# Congo Prime Blog Management System

## Phase 1 technical architecture report and implementation plan

Date: 2026-11-16

## Executive summary

The current website is a static Cloudflare Pages-style asset deployment. The repository
contains the complete public site, including five blog articles, duplicated article
templates, a blog listing, and Cloudflare `_redirects` rules. There is no evidence in
the repository of a Hostinger VPS deployment, Nginx configuration, systemd service,
PostgreSQL database, or GitHub Actions workflow.

The safe target architecture is a separate Django project and private repository,
deployed independently under `/opt/congoprime-blog/`, with PostgreSQL, Gunicorn, and
Nginx routing only the blog and administration host. The existing static site must
remain the owner of all non-blog paths.

Production changes are blocked until the actual VPS document root, active web server,
deployment mechanism, confirmed domain configuration, and backup state are verified.

## Verified repository findings

### Site and deployment

- `wrangler.jsonc` declares a Cloudflare asset deployment with the repository root as
  the assets directory and `404-page` not-found handling.
- `package.json` contains only a local Node preview command: `node server.js`.
- `server.js` is a static file server on port 8080. It maps clean blog paths to
  root-level HTML files and redirects five legacy filenames.
- `_redirects` contains Cloudflare-style 200 rewrites from clean blog URLs to the
  root-level article files, plus five 301 legacy URL redirects.
- No `.github` directory, CI workflow, Docker configuration, Nginx configuration,
  systemd unit, Gunicorn configuration, or database configuration is tracked.
- `.gitignore` states that the repository is synced as public website content, so
  Django code, secrets, media, and database data must not be added here.

### Existing public blog URLs

Canonical listing:

- `/blog.html`

Canonical article paths:

- `/blog/construction-and-infrastructure-development-lubumbashi`
- `/blog/emerging-housing-design-trends-kolwezi`
- `/blog/10-points-designing-home-interior`
- `/blog/building-solid-ground-land-acquisition-permits-haut-katanga`
- `/blog/engineering-katanga-homes-defeat-wet-season`

Legacy filenames currently redirected by `_redirects` and `server.js` include
`/congo-prime-infrastructure-blog-updated.html`,
`/congo-prime-kolwezi-housing-blog-updated.html`,
`/10-points-blog.html`,
`/land-acquisition-and-construction-permits-haut-katanga.html`, and
`/residential-structural-engineering-greater-katanga.html`.

The root article files are the effective rewrite targets and contain absolute
`https://congoprime.com/blog/...` canonical URLs. The corresponding
`blog/<slug>/index.html` copies use relative canonical URLs and should not be used as
the Django migration source without an explicit comparison.

### Design and content

- The listing and article pages share the existing header, navigation, footer, CSS,
  fonts, social links, and responsive layout.
- The article templates use server-rendered HTML, Bootstrap-style layout classes,
  featured images, breadcrumbs, related articles, and client-side share controls.
- The listing uses `js/blog.js` for query-string search and category filtering. Its
  visible categories include construction, infrastructure, architecture,
  interior-design, hospitality, residential, and commercial.
- The repository has English blog content only. French appears in brochure links, but
  no French blog article, language switcher, `hreflang`, or `lang="fr"` article was
  found.
- Article metadata includes title, description, canonical URL, Open Graph data,
  article publication date, featured-image alt text, BlogPosting JSON-LD, and
  BreadcrumbList JSON-LD. Article dates in source files are February-June 2025,
  while listing card dates currently show November 2026; these must be reconciled
  during import rather than silently changed.
- Exact date discrepancy: source metadata is 2025-02-10 (Lubumbashi), 2025-03-15
  (Kolwezi), 2025-04-20 (interior), 2025-05-05 (Haut-Katanga permits), and
  2025-06-12 (wet season). The listing shows 11 Oct 2026 for the first three
  entries and 2 Nov 2026 for the last two. The listing also uses uppercase editorial
  card labels for the last two instead of their article titles. No date was selected
  as authoritative.
- `sitemap.xml` contains 26 URLs, including `/blog.html` and the five clean article
  URLs, and excludes `blog-detail.html`. It is currently a committed static file.
- `robots.txt` allows the site and disallows internal/static utility directories and
  `blog-detail.html`.

### Media

Blog images currently live under `images/blog/` in the public repository, including
WebP and JPG files. New Django uploads must instead use persistent storage outside
the static deployment directory, such as `/var/lib/congoprime-blog/media/`, with
validated image content, size limits, generated safe names, and a backup policy.

## Unverified items and blockers

The repository cannot establish:

1. the Hostinger VPS IP address or SSH access path;
2. the actual static-site document root on the VPS;
3. whether Nginx, Apache, Cloudflare Pages, or another origin is active;
4. the current Nginx virtual hosts, proxy rules, and TLS mode;
5. the active GitHub-to-VPS deployment mechanism, if any;
6. the current Cloudflare DNS records, proxy status, or SSL mode;
7. whether `admin.congoprime.com` exists;
8. current production backups and restore procedures;
9. whether the public domain currently resolves from this environment.

A non-destructive HTTPS probe from this environment timed out, so no live-server
behavior is inferred from that result.

## Proposed target architecture

### Repository and process isolation

- Private repository: a new Django blog repository, separate from `testing-`.
- Application path: `/opt/congoprime-blog/`.
- Virtual environment and release files: owned by a dedicated service account.
- Uploaded media: `/var/lib/congoprime-blog/media/`, never inside either Git checkout.
- PostgreSQL: local/private database with no public listener.
- Gunicorn: Unix socket or localhost-only listener.
- systemd: dedicated `congoprime-blog.service`.
- Nginx: narrowly scoped locations for blog routes, admin hostname, static assets,
  and media; all unrelated paths continue to the existing static origin.
- Cloudflare: DNS and Full (strict) TLS only after domain, certificate, and origin
  configuration are confirmed and approved.

### Django application

Use Django authentication plus explicit groups and model/view permissions:

- `ADMIN`: full content, taxonomy, users, settings, and publishing access.
- `BLOG_EDITOR`: create/edit permitted content, upload images, save drafts, preview,
  and submit for approval; no user or server/settings administration.

Core models should include `BlogPost`, `Category`, `Tag`, `AuthorProfile`, and
translation linkage. `BlogPost` should enforce a unique slug, language, workflow
status, publication timestamps, legacy URL, rich content, featured/OG images, alt
text, and SEO fields. Publishing must be an explicit backend-authorized transition.

### Public rendering and compatibility

Django should render complete HTML using templates adapted from the existing blog
listing and article files. It should own only:

- `/blog.html`;
- `/blog/<slug>`;
- confirmed legacy blog routes;
- the admin hostname and admin paths;
- sitemap generation for published posts.

All other static pages remain served by the existing static deployment. The final
Nginx rules must be tested for route precedence so a blog deployment cannot capture
homepage, service, project, contact, asset, or unrelated legacy paths.

### SEO and sitemap

Every published post must render language, canonical, description, Open Graph,
Twitter/share metadata, image alt text, breadcrumbs, internal links, and BlogPosting
JSON-LD. Drafts must return no public page and must not enter the sitemap. Sitemap
generation should be database-backed and regenerated transactionally or through a
safe post-publish job, with a failure surfaced to administrators.

### Migration

Create a dry-run importer that parses the five root-level article files, extracts
metadata/content/images/links, detects duplicate slugs and URLs, and emits an
exception report for any content that cannot be mapped exactly. Import into a staging
database first. Do not delete or rewrite the existing HTML files until staging,
visual comparison, URL checks, and owner approval succeed.

## Ordered implementation plan

1. **Complete infrastructure discovery**: owner supplies safe read-only VPS command
   output or temporary approved access; verify origin, document root, web server,
   deployment, DNS, Cloudflare, backups, and admin hostname.
2. **Create isolated Django repository**: project settings, environment-based
   configuration, PostgreSQL, authentication, static/media separation, and secure
   production defaults.
3. **Implement domain and workflow models**: posts, translations, categories, tags,
   authors, statuses, permissions, validation, and publish/unpublish transitions.
4. **Build the dashboard**: responsive branded UI for overview, article editing,
   media, taxonomy, search/filter, preview, approval, and user administration.
5. **Adapt public templates**: preserve existing visual structure and assets while
   rendering listing/article pages server-side from published database content.
6. **Implement migration tooling**: dry-run, exact-content checks, duplicate
   detection, staging import, and an explicit exception report.
7. **Implement SEO/sitemap/media controls**: metadata, JSON-LD, sitemap, safe image
   validation/optimization, persistent storage, and backups.
8. **Deploy to staging only**: systemd/Gunicorn/Nginx configuration isolated from the
   static deployment; validate route ownership and HTTPS behavior.
9. **Run acceptance tests**: roles, workflow, media, language, URL compatibility,
   SEO, sitemap, mobile dashboard, static-site regression, deployment isolation, and
   backup restoration.
10. **Production change approval**: obtain explicit approval before DNS changes,
    service restarts, route cutover, or replacing any existing public blog files.

## Phase 1 status

- Inspected: repository history/status, deployment manifests, Node server, redirects,
  blog templates, article metadata/content structure, sitemap, robots, media paths,
  and SEO/deployment notes.
- Built: this report and implementation plan, plus a non-production Django
  foundation outside this repository.
- Modified: `docs/congo-prime-blog-architecture-report.md`. A separate local Django
  project was scaffolded at `D:\congoprime-blog`, outside this public repository.
- Tests performed: read-only repository inspection; no production changes; public
  HTTPS probe timed out and is recorded as unverified.
- Remaining issues: VPS/origin/DNS/Cloudflare/deployment/backup discovery and owner
  confirmation of article dates and domain/admin-hostname strategy. The local Django
  project still needs visual template adaptation, a safe HTML migration importer,
  rich-text editor integration, dashboard workflows, and staging deployment design.
- Production approval: required before any production configuration or DNS change.
