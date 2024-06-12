# asgi.py

# Import necessary modules
import os  # Import os module for interacting with the operating system
from django.core.asgi import get_asgi_application  # Import the ASGI application handler from Django

# Set the default settings module for the 'django' program
# This environment variable tells Django which settings file to use
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "connectify.settings")

# Create the ASGI application instance
# This function loads the Django application to handle web requests asynchronously
application = get_asgi_application()
