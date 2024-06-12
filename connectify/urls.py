# Import necessary modules from Django
from django.contrib import admin  # Import the admin site
from django.urls import path, include  # Import path and include for URL routing
from django.conf import settings  # Import settings to access project settings
from django.conf.urls.static import static  # Import static for serving static and media files

# Define the URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('ckeditor5/', include('django_ckeditor_5.urls')),  # CKEditor URLs for rich text editing
    path('', include('social_posts.urls')),  # Include the URLs from the social_posts app
    path('accounts/', include('user_accounts.urls')),  # Include the URLs from the user_accounts app
]

# If the project is in DEBUG mode, serve static and media files through Django
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Serve static files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files
