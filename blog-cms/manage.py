#!/usr/bin/env python
"""Congo Prime Blog CMS management utility."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'congoprime_cms.settings.development')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Activate your virtual environment or install it."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

