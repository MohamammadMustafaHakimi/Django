"""
ASGI config for myproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

# it stands for asynchronous gateway interface
# this is the standard for python asynchronous web servers, frameworks and applications to communicate with each other
# it is like a bridge between Django and asynchronous features, like websockets and logn lived connections
# it allows django to handle real time interactions, like chat applications and live interfaces, which is done by connecting with a synchrnous python web servers and Frameworks
# it is a technology that enables Django to stay responsive and handle multiple requests in the same time


import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

application = get_asgi_application()
