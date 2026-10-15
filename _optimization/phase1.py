import os, re, hashlib, json, csv, shutil, sys, time
from pathlib import Path
from PIL import Image

ROOT = Path(r'D:\prime-main')
IMAGES_DIR = ROOT / 'images'
REPORTS_DIR = ROOT / '_optimization' / 'reports'
QUARANTINE_DIR = ROOT / '_optimization' / 'quarantine'
WEBP_DIR = ROOT / '_optimization' / 'webp_converted'
MANIFEST_PATH = REPORTS_DIR / 'conversion_manifest.json'

for d in [REPORTS_DIR, QUARANTINE_DIR, WEBP_DIR]:
    d.mkdir(parents=True, exist_ok=True)

CONVERT_EXTS = {'.jpg', '.jpeg', '.png'}
KEEP_AS_IS = {'.svg', '.ico', '.gif', '.webp'}
IMAGE_EXTS_ALL = CONVERT_EXTS | KEEP_AS_IS | {'.bmp', '.tiff', '.tif'}
SCAN_EXTS = {'.html', '.css', '.js', '.json', '.jsonc', '.php'}
SKIP_DIRS = {'_optimization', '.git', 'node_modules'}

HTML_FILES = sorted(ROOT.rglob('*.html')) + sorted(ROOT.rglob('*.php'))
print(f'[AUDIT] Root: {ROOT}')
print(f'[AUDIT] HTML files found: {len(HTML_FILES)}')

# ─ PHASE 1: INVENTORY ─────────────────────────────────────────────────────────
def sha1(path):
    h = hashlib.sha1()
    try:
        with open(path, 'rb') as f:
            for chunk in iter(lambda: f.read(65536), b''):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return 'ERROR'

def image_info(path):
    info = {
        'path': str(path.relative_to(ROOT)).replace('\\', '/'),
        'abs': str(path),
        'ext': path.suffix.lower(),
        'size_bytes': path.stat().st_size,
        'size_kb': round(path.stat().st_size / 1024, 1),
        'sha1': sha1(path),
        'width': None, 'height': None,
        'has_alpha': False, 'is_animated': False
    }
    if path.suffix.lower() in CONVERT_EXTS | {'.webp'}:
        try:
            with Image.open(path) as img:
                info['width'], info['height'] = img.size
                info['has_alpha'] = img.mode in ('RGBA', 'LA', 'P')
                try:
                    img.seek(1)
                    info['is_animated'] = True
                except EOFError:
                    pass
        except Exception as e:
            info['error'] = str(e)
    return info

print('\n[PHASE 1] Building image inventory...')
all_images = []
hash_map = {}
for img_path in IMAGES_DIR.rglob('*'):
    if img_path.is_file() and img_path.suffix.lower() in IMAGE_EXTS_ALL:
        info = image_info(img_path)
        all_images.append(info)
        h = info['sha1']
        hash_map.setdefault(h, []).append(info['path'])

print(f'  Total image assets: {len(all_images)}')
inv_path = REPORTS_DIR / 'image_inventory.csv'
with open(inv_path, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['path','ext','size_bytes','size_kb','width','height','has_alpha','is_animated','sha1'])
    w.writeheader()
    for i in all_images:
        w.writerow({k: i.get(k, '') for k in w.fieldnames})
print(f'  Inventory -> {inv_path}')

duplicates = {h: paths for h, paths in hash_map.items() if len(paths) > 1}
with open(REPORTS_DIR / 'duplicates.json', 'w') as f:
    json.dump(duplicates, f, indent=2)
print(f'  Duplicate groups: {len(duplicates)}')
