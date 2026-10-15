# -*- coding: utf-8 -*-
import os, re, posixpath, json

ROOT = r"D:\prime-main"

GENUINE_PAGES = [
 "index.html","about.html","services.html",
 "Project-Planning-Development.html","Design-Build-Turnkey-Solutions.html",
 "Civil-Structural-Works.html","MEP.html",
 "Site-Preparation-Infrastructure-Enablement.html","Interior-Design-Fit-out-Finishing.html",
 "projects.html","Commercial-projects.html","Residential-projects.html",
 "Industrial-projects.html","Hospitality-Projects.html","Reconstruction-projects.html",
 "projects-detail.html","blog.html","blog-detail.html","10-points-blog.html",
 "congo-prime-infrastructure-blog-updated.html","congo-prime-kolwezi-housing-blog-updated.html",
 "contact-2.html",
]
GENUINE_CSS = ["css/style.css","css/responsive.css","css/color.css"]

ATTR_RE = re.compile(r'(?:src|href|data-src|data-thumb|poster)\s*=\s*["\']([^"\']+\.(?:jpg|jpeg|png|webp|gif|svg))["\']', re.I)
CSS_URL_RE = re.compile(r'url\(\s*["\']?([^"\')]+\.(?:jpg|jpeg|png|webp|gif|svg))["\']?\s*\)', re.I)

def resolve(ref, source_rel_path):
    if ref.startswith(('http://','https://','//','data:')):
        return None
    base_dir = posixpath.dirname(source_rel_path.replace('\\','/'))
    return posixpath.normpath(posixpath.join(base_dir, ref))

missing = {}  # resolved_path -> set of source files that reference it
for rel in GENUINE_PAGES:
    full = os.path.join(ROOT, rel)
    if not os.path.exists(full):
        continue
    with open(full, encoding="utf-8", errors="ignore") as f:
        content = f.read()
    for m in ATTR_RE.finditer(content):
        resolved = resolve(m.group(1), rel)
        if resolved is None:
            continue
        full_path = os.path.join(ROOT, resolved.replace('/', os.sep))
        if not os.path.exists(full_path):
            missing.setdefault(resolved, set()).add(rel)

for rel in GENUINE_CSS:
    full = os.path.join(ROOT, rel)
    if not os.path.exists(full):
        continue
    with open(full, encoding="utf-8", errors="ignore") as f:
        content = f.read()
    for m in CSS_URL_RE.finditer(content):
        resolved = resolve(m.group(1), rel)
        if resolved is None:
            continue
        full_path = os.path.join(ROOT, resolved.replace('/', os.sep))
        if not os.path.exists(full_path):
            missing.setdefault(resolved, set()).add(rel)

print(f"Unique missing resolved paths referenced by genuine pages/CSS: {len(missing)}\n")
out = {}
for path in sorted(missing):
    srcs = sorted(missing[path])
    out[path] = srcs
    print(path, "<-", len(srcs), "pages, e.g.", srcs[:3])

with open(os.path.join(ROOT,"_optimization","genuine_missing.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, indent=1)
