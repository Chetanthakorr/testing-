import json, re
from pathlib import Path

ROOT = Path(r'D:\prime-main')
REPORTS_DIR = ROOT / '_optimization' / 'reports'

with open(REPORTS_DIR / 'broken_references.json') as f:
    broken = json.load(f)

# Re-check which are now fixed
still_broken = []
for b in broken:
    abs_path = ROOT / b['resolved']
    if not abs_path.exists():
        still_broken.append(b)

# Categorize by type
git_deleted_patterns = [
    'background/1.png','background/10.jpg','background/11.jpg','background/13.jpg',
    'background/14.jpg','background/15.jpg','background/2.jpg','background/3.png',
    'background/4.jpg','background/5.jpg','background/6.jpg','background/7.jpg',
    'background/8.jpg','background/9.jpg','gallery/','main-slider/image-1.jpg',
    'main-slider/image-111','main-slider/image-13','main-slider/image-14',
    'main-slider/image-2.','main-slider/image-3.','main-slider/image-4.',
    'main-slider/image-5.','main-slider/image-6.','main-slider/image-7.',
    'main-slider/image-8.','main-slider/image-9.',
    'resource/about-1','resource/about-2','resource/about-3','resource/approach',
    'resource/author-1','resource/author-2','resource/author-3','resource/experiance',
    'resource/faq-img','resource/help','resource/home-seven','resource/image-1.png',
    'resource/image-2.jpg','resource/image-3.jpg','resource/news-','resource/paypall',
    'resource/post-thumb','resource/products/'
]
css_internal = ['css/images/']  # CSS files referencing their own images/ subfolder

pre_existing = []
pre_existing_unique = set()
new_issues = []
for b in still_broken:
    r = b['resolved']
    if any(pat in r for pat in git_deleted_patterns) or any(pat in r for pat in css_internal):
        key = r
        if key not in pre_existing_unique:
            pre_existing_unique.add(key)
            pre_existing.append(b)
    else:
        new_issues.append(b)

print(f'Still broken after WebP fix: {len(still_broken)}')
print(f'  Pre-existing (git-deleted / never existed): {len(pre_existing)} unique paths')
print(f'  New/unexpected issues: {len(new_issues)}')
if new_issues:
    unique_new = list({b['resolved']: b for b in new_issues}.values())
    print('New issues (unique resolved paths):')
    for b in unique_new[:30]:
        print(f'  [{b["source"]}] -> {b["resolved"]}')

# Save updated broken list
with open(REPORTS_DIR / 'broken_refs_after_fix.json', 'w') as f:
    json.dump({'pre_existing': pre_existing, 'new_issues': new_issues,
               'total_still_broken': len(still_broken)}, f, indent=2)
