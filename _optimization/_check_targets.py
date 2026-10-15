import json

br = json.load(open('_optimization/reports/broken_references.json'))
targets = [
    'images/congoprime construction.svg', 'images/background/6.jpg',
    'images/background/process-bg.jpg', 'images/resource/testy-blue (1).png',
    'images/resource/testy-yellow (1).png', 'images/background/4.jpg',
    'images/gallery/17.jpg', 'images/resource/author-3.jpg',
    'images/resource/news-11.jpg', 'images/resource/post-thumb-1.jpg',
]
resolved_set = set(b['resolved'].replace('\\', '/') for b in br)
for t in targets:
    print(t, '-> pre-existing?', t in resolved_set)
