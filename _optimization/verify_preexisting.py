import json
from pathlib import Path

ROOT = Path(r'D:\prime-main')
REPORTS_DIR = ROOT / '_optimization' / 'reports'

# Check all "new issues" to see if they existed before our changes
# Key question: did they exist as ORIGINAL files (jpg/png) or were they already gone?
issues_to_check = [
    'images/services/civil-structural-1.jpg',
    'images/services/civil-structural-2.jpg', 
    'images/services/civil-structural-3.jpg',
    'images/clients/1.png',
    'images/clients/2.png',
    'images/main-slider/image-10.png',
    'images/main-slider/image-11.jpg',
    'images/main-slider/image-12.jpg',
    'images/services/site-preparation-1.jpg',
    'images/background/process-bg.jpg',
    'js/images/icons/map-marker.png',
]

print('Checking if files exist or existed (original jpg/png):')
for p in issues_to_check:
    abs_p = ROOT / p
    exists = abs_p.exists()
    # Also check if we converted this to webp (it would mean we touched it)
    webp_version = abs_p.with_suffix('.webp')
    webp_exists = webp_version.exists()
    print(f'  {p}: exists={exists}, webp_exists={webp_exists}')

# Check images/clients and images/services directories
print()
print('images/clients/ contents:')
clients_dir = ROOT / 'images' / 'clients'
if clients_dir.exists():
    for f in clients_dir.iterdir():
        print(f'  {f.name} ({f.stat().st_size} bytes)')
else:
    print('  (directory does not exist)')

print()
print('images/services/ contents:')
services_dir = ROOT / 'images' / 'services'
if services_dir.exists():
    for f in services_dir.iterdir():
        print(f'  {f.name}')
else:
    print('  (directory does not exist)')
