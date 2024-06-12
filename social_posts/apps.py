# apps.py

# Import the AppConfig class from django.apps
from django.apps import AppConfig


# Define the configuration class for the social_posts app
class SocialPostsConfig(AppConfig):
    # Set the default primary key field type for models in this app
    default_auto_field = "django.db.models.BigAutoField"

    # Define the name of the app
    name = "social_posts"
