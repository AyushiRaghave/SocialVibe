# Import the necessary module from Django
from django.apps import AppConfig

# Define the application configuration class for the 'user_accounts' application
class UserAccountsConfig(AppConfig):
    # Specify the default field type for automatically generated primary keys
    default_auto_field = "django.db.models.BigAutoField"
    
    # Name of the application. This is used by Django to refer to the app.
    name = "user_accounts"
    