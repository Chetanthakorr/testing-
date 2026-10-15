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

STYLE_URL_RE = re.compile(r'style\s*=\s*"[^"]*url\(\s*([^"\')]+\.(?:jpg|jpeg|png|webp|gif))\s*\)[^"]*"', re.I)

def resolve(ref, source_rel_path):
    if ref.startswith(('http://','https://','//','data:')):
        return None
    base_dir = posixpath.dirname(source_rel_path.replace('\\','/'))
    return posixpath.normpath(posixpath.join(base_dir, ref))

missing = {}
total = 0
for rel in GENUINE_PAGES:
    full = os.path.join(ROOT, rel)
    if not os.path.exists(full):
        continue
    with open(full, encoding="utf-8", errors="ignore") as f:
        content = f.read()
    for m in STYLE_URL_RE.finditer(content):
        ref = m.group(1)
        resolved = resolve(ref, rel)
        if resolved is None:
            continue
        total += 1
        full_path = os.path.join(ROOT, resolved.replace('/', os.sep))
        if not os.path.exists(full_path):
            missing.setdefault(resolved, set()).add(rel)

print(f"Total inline style background-image refs checked: {total}")
print(f"Unique missing: {len(missing)}\n")
for path in sorted(missing):
    print(path, "<-", sorted(missing[path]))
