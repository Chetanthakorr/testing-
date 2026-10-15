import json
from pathlib import Path
ROOT = Path(r'D:\prime-main')
REPORTS_DIR = ROOT / '_optimization' / 'reports'

with open(REPORTS_DIR / 'broken_references.json') as f:
    broken = json.load(f)

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
    'resource/post-thumb','resource/products/','services/'
]

pre_existing = []
regressions = []
for b in broken:
    r = b['resolved']
    is_pre = any(pat in r for pat in git_deleted_patterns)
    if r.endswith('.webp'):
        regressions.append(b)
    elif is_pre:
        pre_existing.append(b)
    else:
        regressions.append(b)

print('Total broken:', len(broken))
print('Pre-existing (git-deleted/never-existed):', len(pre_existing))
print('Potential regressions (our changes):', len(regressions))
webp_missing = [b for b in regressions if b['resolved'].endswith('.webp')]
print('  - Missing WebP files:', len(webp_missing))
print()
if regressions:
    print('Regression details (first 30):')
    unique_reg = list({b['resolved']: b for b in regressions}.values())[:30]
    for b in unique_reg:
        print(' ', b['source'], '->', b['resolved'])
