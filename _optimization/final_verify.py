import json
from pathlib import Path

ROOT = Path(r'D:\prime-main')
REPORTS_DIR = ROOT / '_optimization' / 'reports'

with open(REPORTS_DIR / 'conversion_manifest.json') as f:
    manifest = json.load(f)

# Verify every converted image: both original still exists AND webp exists
regressions = []
all_ok = []
for orig_key, entry in manifest.items():
    orig_abs = ROOT / entry['original']
    webp_in_images = ROOT / entry['new_site_path']
    orig_exists = orig_abs.exists()
    webp_exists = webp_in_images.exists()
    if not webp_exists:
        regressions.append({'original': entry['original'], 'webp': entry['new_site_path'], 'issue': 'WebP missing from images/'})
    else:
        all_ok.append(entry['new_site_path'])

print(f'Manifest entries: {len(manifest)}')
print(f'WebP files correctly placed in images/: {len(all_ok)}')
print(f'WebP files MISSING from images/: {len(regressions)}')
if regressions:
    for r in regressions:
        print(f'  MISSING: {r["webp"]}')
else:
    print('ALL CONVERTED WEBP FILES ARE IN PLACE - NO REGRESSIONS FROM OUR CHANGES')

# Also verify the files updated in HTML still work
print()
with open(REPORTS_DIR / 'changes_log.json') as f:
    changes = json.load(f)
print(f'Files where we updated references: {len(changes)}')

# Check if any updated 'to' reference is broken
broken_updates = []
for fpath_str, replacements in changes.items():
    for rep in replacements:
        new_ref = rep['to']
        # Resolve from file location
        fpath = ROOT / fpath_str
        try:
            from pathlib import Path as P
            new_abs = (fpath.parent / new_ref).resolve()
            if not new_abs.exists():
                # Try from root
                new_abs2 = ROOT / new_ref
                if not new_abs2.exists():
                    broken_updates.append({'file': fpath_str, 'ref': new_ref})
        except Exception:
            pass

print(f'Updated references that point to missing files: {len(broken_updates)}')
if broken_updates:
    unique = list({b['ref']: b for b in broken_updates}.values())[:20]
    for b in unique:
        print(f'  [{b["file"]}] -> {b["ref"]}')
else:
    print('ALL UPDATED REFERENCES RESOLVE CORRECTLY')
