# settings.py

# Import necessary modules from Python's standard library
from pathlib import Path  # Path is used for file path manipulations
import os  # os module provides a way of using operating system dependent functionality
from decouple import config, Csv  # decouple helps to separate settings from code, config reads the .env file
import dj_database_url  # dj_database_url helps to configure the database using a single URL

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'user_accounts',
    'social_posts',
    'django_ckeditor_5',
    'crispy_forms',
    'crispy_bootstrap4',
]


# Configuration for CKEditor
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            'heading', '|', 'bold', 'italic', 'link', 'bulletedList', 'numberedList', 'blockQuote', '|',
            'insertTable', 'mediaEmbed', 'undo', 'redo'
        ],
        'height': 300,
        'width': '100%',
    },
}


# Crispy forms settings
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap4'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Middleware settings, middleware is a way to process requests globally before they reach the view
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",  # Provides security enhancements
    "django.contrib.sessions.middleware.SessionMiddleware",  # Manages sessions across requests
    "django.middleware.common.CommonMiddleware",  # Performs various common operations
    "django.middleware.csrf.CsrfViewMiddleware",  # Prevents Cross-Site Request Forgery attacks
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # Associates users with requests using sessions
    "django.contrib.messages.middleware.MessageMiddleware",  # Enables cookie- and session-based messaging
    "django.middleware.clickjacking.XFrameOptionsMiddleware",  # Prevents clickjacking
]
# URL configuration
ROOT_URLCONF = "connectify.urls"  # Points to the module where URL patterns are defined

# Template settings
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",  # Use Django's template engine
        "DIRS": [os.path.join(BASE_DIR, 'templates')],  # List of directories to search for templates
        "APP_DIRS": True,  # Whether to look for templates in application directories
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",  # Adds debug information to templates
                "django.template.context_processors.request",  # Adds request object to context
                "django.contrib.auth.context_processors.auth",  # Adds user and permissions to context
                "django.contrib.messages.context_processors.messages",  # Adds messages to context
            ],
        },
    },
]
# WSGI application, entry-point for WSGI-compatible web servers to serve your project
WSGI_APPLICATION = "connectify.wsgi.application"

# Database configuration
DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))  # Configures the database using a URL from .env
}

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization settings
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True  # Enables Django's translation system
USE_TZ = True  # Enables timezone-aware datetimes

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Email backend configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

# Authentication redirects
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'
