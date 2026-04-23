#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# this is a command line utility that coes with every django project
# we will use it for instance to create our first applications
# it provides varoius commands for performing common tasks such as creating database tables, running development servers, creating super users, and also it helps with running tests
# it basically acts as a wrapper around Django's adminstrativ tasks

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
