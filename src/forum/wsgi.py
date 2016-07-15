import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "forum.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
