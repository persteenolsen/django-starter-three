"""
WSGI config for vercel_app project.

It exposes the WSGI callable as a module-level variable named ``app``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vercel_app.settings')

app = get_wsgi_application()

# Note: It seems that it is not needed !
#app = WhiteNoise(app, root=os.path.join(os.path.dirname(__file__), 'static'))

