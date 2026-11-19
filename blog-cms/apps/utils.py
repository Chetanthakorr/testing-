"""
Shared utilities for Congo Prime Blog CMS
"""
import re
import unicodedata


def slugify(value: str) -> str:
    """
    Convert a string to a URL-safe slug.
    Replaces python-slugify (not available in this environment).
    """
    value = str(value)
    # Normalize unicode
    value = unicodedata.normalize('NFKD', value)
    value = value.encode('ascii', 'ignore').decode('ascii')
    value = value.lower()
    value = re.sub(r'[^\w\s-]', '', value)
    value = re.sub(r'[\s_-]+', '-', value)
    value = value.strip('-')
    return value


def unique_slug(model_class, title: str, exclude_pk=None) -> str:
    """Generate a unique slug for a model, appending a number if needed."""
    base = slugify(title)
    slug = base
    n = 1
    qs = model_class.objects.filter(slug=slug)
    if exclude_pk:
        qs = qs.exclude(pk=exclude_pk)
    while qs.exists():
        slug = f'{base}-{n}'
        n += 1
        qs = model_class.objects.filter(slug=slug)
        if exclude_pk:
            qs = qs.exclude(pk=exclude_pk)
    return slug

