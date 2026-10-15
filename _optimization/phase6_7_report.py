import os, re, json, csv, time
from pathlib import Path

ROOT = Path(r'D:\prime-main')
REPORTS_DIR = ROOT / '_optimization' / 'reports'
SCAN_EXTS = {'.html', '.css', '.js', '.json', '.jsonc', '.php'}
SKIP_DIRS = {'_optimization', '.git', 'node_modules'}

with open(REPORTS_DIR / 'conversion_manifest.json') as f:
    conversion_manifest = json.load(f)
with open(REPORTS_DIR / 'classified.json') as f:
    classified = json.load(f)
with open(REPORTS_DIR / 'phase4_stats.json') as f:
    stats = json.load(f)

# ─ PHASE 6: UPDATE REFERENCES ─────────────────────────────────────────────────
print('\n[PHASE 6] Updating image references in source files...')
changes_log = {}

def update_file(fpath):
    try:
        original = fpath.read_text(encoding='utf-8', errors='replace')
    except Exception:
        return 0
    content = original
    file_changes = []
    for orig_key, entry in conversion_manifest.items():
        orig_ref = orig_key
        new_ref = entry['new_site_path']
        if orig_ref in content:
            content = content.replace(orig_ref, new_ref)
            file_changes.append({'from': orig_ref, 'to': new_ref})
        # Handle relative paths (e.g. from nested HTML)
        try:
            fdir = fpath.parent
            orig_abs = (ROOT / orig_key).resolve()
            new_abs = (ROOT / new_ref).resolve()
            rel_orig = os.path.relpath(orig_abs, fdir).replace('\\', '/')
            rel_new = os.path.relpath(new_abs, fdir).replace('\\', '/')
            if rel_orig in content:
                content = content.replace(rel_orig, rel_new)
                file_changes.append({'from': rel_orig, 'to': rel_new})
        except Exception:
            pass
    if content != original:
        fpath.write_text(content, encoding='utf-8')
        changes_log[str(fpath.relative_to(ROOT)).replace('\\', '/')] = file_changes
        return len(file_changes)
    return 0

total_updated = 0
for fpath in ROOT.rglob('*'):
    if fpath.is_file() and fpath.suffix.lower() in SCAN_EXTS:
        if not any(sd in fpath.parts for sd in SKIP_DIRS):
            n = update_file(fpath)
            if n:
                total_updated += 1

print(f'  Files updated: {total_updated}')
with open(REPORTS_DIR / 'changes_log.json', 'w') as f:
    json.dump(changes_log, f, indent=2)

# ─ PHASE 7: VALIDATION ────────────────────────────────────────────────────────
print('\n[PHASE 7] Validating image references post-migration...')
IMG_PATTERNS = [
    re.compile(r'(?:src|href|srcset|poster|data-src|data-original|data-bg|content)\s*=\s*["\']([^"\']+\.(?:jpg|jpeg|png|gif|webp|svg|ico|bmp|tiff?))["\']', re.I),
    re.compile(r'url\(["\']?([^"\')\s]+\.(?:jpg|jpeg|png|gif|webp|svg|ico|bmp|tiff?))["\']?\)', re.I),
    re.compile(r'["\']([^"\']*images/[^"\']+\.(?:jpg|jpeg|png|gif|webp|svg|ico))["\']', re.I),
]

def resolve_img_ref(raw_ref, source_file):
    raw_ref = raw_ref.split('?')[0].split('#')[0].strip()
    if raw_ref.startswith(('http://', 'https://', 'data:', '//')):
        return None
    p = raw_ref.replace('\\', '/')
    if p.startswith('/'):
        p = p.lstrip('/')
    try:
        resolved = (source_file.parent / p).resolve()
        return str(resolved.relative_to(ROOT.resolve())).replace('\\', '/')
    except Exception:
        try:
            resolved = (ROOT / p).resolve()
            return str(resolved.relative_to(ROOT.resolve())).replace('\\', '/')
        except Exception:
            return p

broken = []
ok_count = 0
for fpath in ROOT.rglob('*'):
    if fpath.is_file() and fpath.suffix.lower() in SCAN_EXTS:
        if not any(sd in fpath.parts for sd in SKIP_DIRS):
            try:
                content = fpath.read_text(encoding='utf-8', errors='replace')
            except Exception:
                continue
            for pat in IMG_PATTERNS:
                for m in pat.finditer(content):
                    raw = m.group(1)
                    if raw.startswith(('http', 'data:', '//')):
                        continue
                    resolved = resolve_img_ref(raw, fpath)
                    if resolved and 'images/' in resolved.replace('\\', '/'):
                        abs_path = ROOT / resolved
                        if abs_path.exists():
                            ok_count += 1
                        else:
                            broken.append({
                                'ref': raw,
                                'resolved': resolved,
                                'source': str(fpath.relative_to(ROOT)).replace('\\', '/')
                            })

print(f'  Valid refs: {ok_count}')
print(f'  Broken refs: {len(broken)}')
with open(REPORTS_DIR / 'broken_references.json', 'w') as f:
    json.dump(broken, f, indent=2)

if broken:
    for b in broken[:15]:
        print(f'    BROKEN: {b["source"]} -> {b["resolved"]}')

# ─ FINAL REPORT ───────────────────────────────────────────────────────────────
print('\n' + '='*70)
print('FINAL REPORT')
print('='*70)

all_images_count = len(classified)
all_orig_kb = sum(float(i.get('size_kb', 0)) for i in classified)
unused_quarantined = sum(1 for i in classified if i.get('category') == 'C')
with open(REPORTS_DIR / 'duplicates.json') as f:
    dups = json.load(f)

report = {
    'timestamp': time.strftime('%Y-%m-%dT%H:%M:%S'),
    'total_assets_scanned': all_images_count,
    'images_converted_to_webp': stats['converted_count'],
    'conversion_failures': stats['failures'],
    'conversion_skipped': stats['skipped'],
    'original_total_kb': round(all_orig_kb, 1),
    'webp_total_kb': round(stats['webp_bytes_total']/1024, 1),
    'size_saved_kb': round(all_orig_kb - stats['webp_bytes_total']/1024, 1),
    'size_saved_pct': round((1 - stats['webp_bytes_total']/(stats['orig_bytes_total'] or 1))*100, 1),
    'confirmed_unused_quarantined': unused_quarantined,
    'duplicate_groups': len(dups),
    'broken_references_post_migration': len(broken),
    'valid_references': ok_count,
    'files_updated': total_updated,
    'rollback': 'git -C D:/prime-main checkout main',
    'remaining_manual_tasks': [
        'Browser-test all pages visually',
        'Verify slider/gallery/lightbox rendering',
        'Review category B assets in unused-assets-candidates.csv',
        'Review git-deleted files (shown as D in git status) - not on disk',
        'Sign off and permanently delete _optimization/quarantine/ when safe',
        'Review public_html/ and store/ if deployed separately',
    ]
}
with open(REPORTS_DIR / 'final_report.json', 'w') as f:
    json.dump(report, f, indent=2)

for k, v in report.items():
    if k != 'remaining_manual_tasks':
        print(f'  {k:40s}: {v}')
print('\n  Remaining manual tasks:')
for t in report['remaining_manual_tasks']:
    print(f'    - {t}')
print('='*70)
print('DONE. Branch: image-optimization-webp')
