import json, shutil, os
from pathlib import Path

ROOT = Path(r'D:\prime-main')
REPORTS_DIR = ROOT / '_optimization' / 'reports'

with open(REPORTS_DIR / 'broken_references.json') as f:
    broken = json.load(f)

# Find all unique missing WebP targets
missing_webp = set()
for b in broken:
    if b['resolved'].endswith('.webp'):
        missing_webp.add(b['resolved'])

print(f'Unique missing WebP targets: {len(missing_webp)}')

# For each missing WebP, check if it exists elsewhere (root images/)
fixed = 0
still_missing = []
for rel_path in sorted(missing_webp):
    abs_path = ROOT / rel_path
    if abs_path.exists():
        continue  # not actually missing
    
    # Try to find the webp in root images/ (without public_html/ prefix)
    # e.g. public_html/images/background/12.webp -> images/background/12.webp
    stripped = rel_path.replace('public_html/images/', 'images/').replace('public_html\\images\\', 'images/')
    source_in_root = ROOT / stripped
    
    if source_in_root.exists():
        abs_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_in_root, abs_path)
        fixed += 1
    else:
        # Try store/images/
        stripped2 = rel_path.replace('store/images/', 'images/')
        source2 = ROOT / stripped2
        if source2.exists():
            abs_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source2, abs_path)
            fixed += 1
        else:
            still_missing.append(rel_path)

print(f'Fixed by copying WebP: {fixed}')
print(f'Still missing: {len(still_missing)}')
if still_missing:
    print('Still missing (first 20):')
    for p in still_missing[:20]:
        print(' ', p)
