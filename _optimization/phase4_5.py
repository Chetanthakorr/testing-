import os, re, json, csv, shutil, time
from pathlib import Path
from PIL import Image

ROOT = Path(r'D:\prime-main')
REPORTS_DIR = ROOT / '_optimization' / 'reports'
QUARANTINE_DIR = ROOT / '_optimization' / 'quarantine'
WEBP_DIR = ROOT / '_optimization' / 'webp_converted'
MANIFEST_PATH = REPORTS_DIR / 'conversion_manifest.json'
CONVERT_EXTS = {'.jpg', '.jpeg', '.png'}
KEEP_AS_IS = {'.svg', '.ico', '.gif', '.webp'}
SCAN_EXTS = {'.html', '.css', '.js', '.json', '.jsonc', '.php'}
SKIP_DIRS = {'_optimization', '.git', 'node_modules'}

with open(REPORTS_DIR / 'classified.json') as f:
    classified = json.load(f)

# ─ PHASE 4: WEBP CONVERSION ──────────────────────────────────────────────────
print('\n[PHASE 4] Converting images to WebP...')
WEBP_QUALITY_PHOTO = 82
WEBP_QUALITY_ALPHA = 85
MIN_SIZE_KB = 8

conversion_manifest = {}
failures = []
skipped = []
converted_count = 0
orig_bytes_total = 0
webp_bytes_total = 0

for info in classified:
    if info['ext'] not in CONVERT_EXTS:
        continue
    if info['category'] not in ('A', 'B'):
        continue
    if info['size_kb'] < MIN_SIZE_KB:
        skipped.append({'path': info['path'], 'reason': f"Too small ({info['size_kb']} KB)"})
        continue
    if info.get('is_animated') == True or info.get('is_animated') == 'True':
        skipped.append({'path': info['path'], 'reason': 'Animated'})
        continue

    src_path = Path(info['abs'])
    if not src_path.exists():
        skipped.append({'path': info['path'], 'reason': 'File not on disk (git-deleted)'})
        continue

    rel = Path(info['path'])
    try:
        inner = rel.relative_to('images')
    except ValueError:
        inner = rel

    webp_rel = inner.with_suffix('.webp')
    webp_abs = WEBP_DIR / webp_rel
    webp_abs.parent.mkdir(parents=True, exist_ok=True)

    try:
        with Image.open(src_path) as img:
            if img.mode == 'P':
                img = img.convert('RGBA')
            elif img.mode == 'CMYK':
                img = img.convert('RGB')
            has_alpha = img.mode in ('RGBA', 'LA')
            quality = WEBP_QUALITY_ALPHA if has_alpha else WEBP_QUALITY_PHOTO
            img.save(webp_abs, 'WEBP', quality=quality, method=6)

        orig_size = src_path.stat().st_size
        webp_size = webp_abs.stat().st_size
        orig_bytes_total += orig_size
        webp_bytes_total += webp_size
        orig_key = info['path'].replace('\\', '/')
        new_img_path = str(rel.parent / webp_rel.name).replace('\\', '/')
        conversion_manifest[orig_key] = {
            'original': orig_key,
            'webp_generated': str(webp_rel).replace('\\', '/'),
            'new_site_path': new_img_path,
            'orig_size_kb': round(orig_size/1024, 1),
            'webp_size_kb': round(webp_size/1024, 1),
            'saving_pct': round((1 - webp_size/orig_size)*100, 1),
            'quality': quality
        }
        converted_count += 1
        if converted_count % 10 == 0:
            print(f'  ... {converted_count} converted')
    except Exception as e:
        failures.append({'path': info['path'], 'error': str(e)})

print(f'  Converted: {converted_count}')
print(f'  Skipped: {len(skipped)}')
print(f'  Failures: {len(failures)}')
if orig_bytes_total:
    pct = round((1 - webp_bytes_total/orig_bytes_total)*100, 1)
    print(f'  {round(orig_bytes_total/1024/1024,1)} MB -> {round(webp_bytes_total/1024/1024,1)} MB ({pct}% saved)')

with open(MANIFEST_PATH, 'w') as f:
    json.dump(conversion_manifest, f, indent=2)
with open(REPORTS_DIR / 'conversion_failures.json', 'w') as f:
    json.dump({'failures': failures, 'skipped': skipped}, f, indent=2)

# ─ PHASE 5: PLACE WEBP FILES ─────────────────────────────────────────────────
print('\n[PHASE 5] Placing WebP files into images/...')
placed = 0
for orig_key, entry in conversion_manifest.items():
    src = WEBP_DIR / entry['webp_generated']
    target = ROOT / 'images' / entry['webp_generated']
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists() and src.exists():
        shutil.copy2(src, target)
        placed += 1
print(f'  Placed {placed} WebP files')

# Save partial stats for final report
stats = {
    'converted_count': converted_count,
    'orig_bytes_total': orig_bytes_total,
    'webp_bytes_total': webp_bytes_total,
    'failures': len(failures),
    'skipped': len(skipped)
}
with open(REPORTS_DIR / 'phase4_stats.json', 'w') as f:
    json.dump(stats, f, indent=2)

print('Phase 4+5 complete.')
