"""
Phase 8 substitute: HTTP-level validation of the 22 genuine pages.
The built-in browser pane cannot reach a localhost server started by this
shell (different host), so this script performs an equivalent check over
real HTTP: fetch each page, parse every asset reference (img src/srcset,
link href, script src, css url()), and confirm each resolves with HTTP 200.
"""
import re
import subprocess
import sys
import time
import json
import urllib.request
import urllib.error
from pathlib import Path
from urllib.parse import urljoin, urlparse

ROOT = Path(r"D:\prime-main")
PORT = 8799
BASE = f"http://127.0.0.1:{PORT}/"

PAGES = [
    "index.html", "about.html", "services.html",
    "Civil-Structural-Works.html", "Design-Build-Turnkey-Solutions.html",
    "Interior-Design-Fit-out-Finishing.html", "MEP.html",
    "Project-Planning-Development.html",
    "Site-Preparation-Infrastructure-Enablement.html",
    "projects.html", "Commercial-projects.html", "Hospitality-Projects.html",
    "Industrial-projects.html", "Reconstruction-projects.html",
    "Residential-projects.html", "projects-detail.html",
    "blog.html", "blog-detail.html", "10-points-blog.html",
    "congo-prime-infrastructure-blog-updated.html",
    "congo-prime-kolwezi-housing-blog-updated.html",
    "contact-2.html",
]

ATTR_RE = re.compile(
    r'(?:src|href|data-src|data-original|poster)=["\']([^"\']+)["\']', re.I)
URL_RE = re.compile(r'url\(([^)]+)\)', re.I)
SRCSET_RE = re.compile(r'srcset=["\']([^"\']+)["\']', re.I)

SKIP_SCHEMES = ("http://", "https://", "//", "mailto:", "tel:", "javascript:", "#", "data:")


def fetch(url, timeout=10):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "phase8-validator"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, b""
    except Exception as e:
        return -1, str(e).encode()


def extract_refs(html_text, base_url):
    refs = set()
    for m in ATTR_RE.finditer(html_text):
        v = m.group(1).strip()
        if v and not v.startswith(SKIP_SCHEMES):
            refs.add(urljoin(base_url, v))
    for m in SRCSET_RE.finditer(html_text):
        parts = m.group(1).split(",")
        for p in parts:
            v = p.strip().split(" ")[0]
            if v and not v.startswith(SKIP_SCHEMES):
                refs.add(urljoin(base_url, v))
    for m in URL_RE.finditer(html_text):
        v = m.group(1).strip().strip("'\"")
        if v and not v.startswith(SKIP_SCHEMES):
            refs.add(urljoin(base_url, v))
    return refs


def main():
    proc = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(PORT)],
        cwd=str(ROOT), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    time.sleep(1.5)
    results = {}
    try:
        all_asset_fail = {}
        for page in PAGES:
            page_url = urljoin(BASE, page)
            status, body = fetch(page_url)
            entry = {"status": status, "assets_checked": 0, "assets_failed": []}
            if status == 200:
                text = body.decode("utf-8", errors="replace")
                refs = extract_refs(text, page_url)
                css_refs = set()
                for r in refs:
                    if r.lower().endswith(".css"):
                        s, b = fetch(r)
                        if s == 200:
                            css_text = b.decode("utf-8", errors="replace")
                            css_refs |= extract_refs(css_text, r)
                refs |= css_refs
                for r in sorted(refs):
                    parsed = urlparse(r)
                    if parsed.netloc and parsed.netloc != f"127.0.0.1:{PORT}":
                        continue
                    s, _ = fetch(r)
                    entry["assets_checked"] += 1
                    if s != 200:
                        entry["assets_failed"].append({"url": r, "status": s})
                if entry["assets_failed"]:
                    all_asset_fail[page] = entry["assets_failed"]
            results[page] = entry
    finally:
        proc.terminate()
        proc.wait(timeout=5)

    out = ROOT / "_optimization" / "reports" / "phase8_http_validation.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")

    total_pages = len(PAGES)
    ok_pages = sum(1 for e in results.values() if e["status"] == 200)
    total_assets = sum(e["assets_checked"] for e in results.values())
    failed_assets = sum(len(e["assets_failed"]) for e in results.values())
    print(f"Pages checked: {total_pages}, HTTP 200: {ok_pages}")
    print(f"Total asset refs checked (HTML+CSS, same-origin): {total_assets}")
    print(f"Failed asset fetches: {failed_assets}")
    if failed_assets:
        for page, fails in results.items():
            if fails["assets_failed"]:
                print(f"  {page}:")
                for f in fails["assets_failed"][:10]:
                    print(f"    {f['status']} {f['url']}")


if __name__ == "__main__":
    main()
