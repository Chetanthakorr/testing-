import os, re, hashlib, json, csv, shutil, sys, time
from pathlib import Path
from PIL import Image

ROOT = Path(r'D:\prime-main')
IMAGES_DIR = ROOT / 'images'
REPORTS_DIR = ROOT / '_optimization' / 'reports'
QUARANTINE_DIR = ROOT / '_optimization' / 'quarantine'
WEBP_DIR = ROOT / '_optimization' / 'webp_converted'
MANIFEST_PATH = REPORTS_DIR / 'conversion_manifest.json'
CONVERT_EXTS = {'.jpg', '.jpeg', '.png'}
KEEP_AS_IS = {'.svg', '.ico', '.gif', '.webp'}
IMAGE_EXTS_ALL = CONVERT_EXTS | KEEP_AS_IS | {'.bmp', '.tiff', '.tif'}
SCAN_EXTS = {'.html', '.css', '.js', '.json', '.jsonc', '.php'}
SKIP_DIRS = {'_optimization', '.git', 'node_modules'}

# Load inventory from phase1
import ast
all_images = []
with open(REPORTS_DIR / 'image_inventory.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        info = dict(row)
        info['size_kb'] = float(info['size_kb']) if info['size_kb'] else 0
        info['has_alpha'] = info['has_alpha'] == 'True'
        info['is_animated'] = info['is_animated'] == 'True'
        info['abs'] = str(ROOT / info['path'].replace('/', os.sep))
        all_images.append(info)

print(f'[PHASE 2] Scanning all source files for image references...')

IMG_PATTERNS = [
    re.compile(r'(?:src|href|srcset|poster|data-src|data-original|data-bg|content)\s*=\s*["\']([^"\']+\.(?:jpg|jpeg|png|gif|webp|svg|ico|bmp|tiff?))["\']', re.I),
    re.compile(r'url\(["\']?([^"\')\s]+\.(?:jpg|jpeg|png|gif|webp|svg|ico|bmp|tiff?))["\']?\)', re.I),
    re.compile(r'["\']([^"\']*images/[^"\']+\.(?:jpg|jpeg|png|gif|webp|svg|ico))["\']', re.I),
]

ref_map = {}

def resolve_img_ref(raw_ref, source_file):
    raw_ref = raw_ref.split('?')[0].split('#')[0].strip()
    if raw_ref.startswith(('http://', 'https://', 'data:', '//')):
        return None
    p = raw_ref.replace('\\', '/')
    if p.startswith('/'):
        p = p.lstrip('/')
    source_dir = source_file.parent
    try:
        resolved = (source_dir / p).resolve()
        rel = resolved.relative_to(ROOT.resolve())
        return str(rel).replace('\\', '/')
    except Exception:
        try:
            resolved = (ROOT / p).resolve()
            rel = resolved.relative_to(ROOT.resolve())
            return str(rel).replace('\\', '/')
        except Exception:
            return p

def scan_file(fpath):
    try:
        content = fpath.read_text(encoding='utf-8', errors='replace')
    except Exception:
        return
    for pat in IMG_PATTERNS:
        for m in pat.finditer(content):
            raw = m.group(1)
            resolved = resolve_img_ref(raw, fpath)
            if resolved and 'images/' in resolved.replace('\\', '/'):
                key = resolved.lower().replace('\\', '/')
                ref_map.setdefault(key, set()).add(str(fpath.relative_to(ROOT)).replace('\\', '/'))

scanned_count = 0
for fpath in ROOT.rglob('*'):
    if fpath.is_file() and fpath.suffix.lower() in SCAN_EXTS:
        if not any(sd in fpath.parts for sd in SKIP_DIRS):
            scan_file(fpath)
            scanned_count += 1

print(f'  Files scanned: {scanned_count}')
print(f'  Unique image refs: {len(ref_map)}')

with open(REPORTS_DIR / 'all_references.json', 'w') as f:
    json.dump({k: list(v) for k, v in ref_map.items()}, f, indent=2)

# ─ PHASE 3: CLASSIFY ──────────────────────────────────────────────────────────
print('\n[PHASE 3] Classifying assets...')
CORE_ASSETS = {'favicon.png','favicon-icon.png','logo.png','logo-2.png','logo-3.png',
               'footer-logo.png','footer-logooo.png','logo-small.png'}

classified = []
confirmed_unused = []
for info in all_images:
    norm = info['path'].lower().replace('\\', '/')
    fname = Path(info['path']).name.lower()
    direct_match = norm in ref_map
    partial_match = any(fname in k for k in ref_map.keys())
    if direct_match or partial_match:
        cat, reason = 'A', 'Direct/partial reference found'
    elif fname in CORE_ASSETS:
        cat, reason = 'A', 'Core site asset'
    elif 'fancybox' in norm:
        cat, reason = 'A', 'Fancybox plugin asset'
    elif info['ext'] in KEEP_AS_IS:
        cat, reason = 'B', f"Special format {info['ext']}"
    else:
        cat, reason = 'C', 'No reference found'
    info['category'] = cat
    info['reason'] = reason
    classified.append(info)
    if cat == 'C':
        confirmed_unused.append(info)

print(f"  A (used): {sum(1 for i in classified if i['category']=='A')}")
print(f"  B (maybe): {sum(1 for i in classified if i['category']=='B')}")
print(f"  C (unused): {sum(1 for i in classified if i['category']=='C')}")

# Save candidates
with open(REPORTS_DIR / 'unused-assets-candidates.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['path','size_kb','category','reason'])
    for i in classified:
        if i['category'] in ('B', 'C'):
            w.writerow([i['path'], i['size_kb'], i['category'], i['reason']])

# Quarantine C assets
quarantine_log = []
for info in confirmed_unused:
    src = Path(info['abs'])
    if not src.exists():
        continue
    dst = QUARANTINE_DIR / info['path']
    dst.parent.mkdir(parents=True, exist_ok=True)
    try:
        shutil.copy2(src, dst)
        quarantine_log.append({'src': info['path'], 'size_kb': info['size_kb']})
    except Exception as e:
        print(f'  WARN: {src}: {e}')

with open(REPORTS_DIR / 'quarantine_log.json', 'w') as f:
    json.dump(quarantine_log, f, indent=2)
print(f'  Quarantined {len(quarantine_log)} assets')

# Save classified for phase4
with open(REPORTS_DIR / 'classified.json', 'w') as f:
    json.dump(classified, f, indent=2)
print('Phase 2+3 complete.')
