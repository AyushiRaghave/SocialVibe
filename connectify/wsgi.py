# wsgi.py

# Import necessary modules
import os  # Import os module for interacting with the operating system
from django.core.wsgi import get_wsgi_application  # Import the WSGI application handler from Django

# Set the default settings module for the 'django' program
# This environment variable tells Django which settings file to use
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "connectify.settings")

# Get the WSGI application callable
# This function loads the Django application to handle web requests
application = get_wsgi_application()

# Alias 'application' to 'app' for compatibility with deployment platforms
# Some platforms expect the WSGI callable to be named 'app' instead of 'application'
app = application
