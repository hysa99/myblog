"""
WSGI config for blogg project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogg.settings')

# Get the Django WSGI application
application = get_wsgi_application()

# Serve static files with WhiteNoise
application = WhiteNoise(application, root="/myblog-master/staticfiles/item_images/")
application.add_files("/myblog-master/staticfiles/item_images/", prefix="more-files/")
