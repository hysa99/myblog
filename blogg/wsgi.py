"""
WSGI config for blogg project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogg.settings')
from whitenoise import WhiteNoise



application = get_wsgi_application()
application = WhiteNoise(application, root="/myblog-master/staticfiles/item_images/")
application.add_files("/myblog-master/staticfiles/item_images/", prefix="more-files/")