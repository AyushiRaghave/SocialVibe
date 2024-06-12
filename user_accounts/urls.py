# Import necessary modules from Django
from django.urls import path
from . import views  # Import views from the current package
from django.views.generic import TemplateView  # Import TemplateView for simple class-based views

# Define the URL patterns for the user_accounts application
urlpatterns = [
    # URL pattern for the user registration view
    path('register/', views.register, name='register'),

    # URL pattern for the user login view
    path('login/', views.user_login, name='login'),

    # URL pattern for the user logout view
    path('logout/', views.user_logout, name='logout'),

    # URL pattern for the user profile view
    path('profile/', views.profile, name='profile'),

    # URL pattern for the delete profile view
    path('delete-profile/', views.delete_profile, name='delete_profile'),

    # URL pattern for the change password view
    path('change-password/', views.change_password, name='change_password'),

    # URL pattern for the email verification view, expects a token as a parameter
    path('verify-email/<str:token>/', views.verify_email, name='verify_email'),

    # URL pattern for the password reset request view
    path('password-reset/', views.password_reset_request, name='password_reset'),

    # URL pattern for the password reset done view, uses TemplateView to render a static template
    path('password-reset/done/', 
         TemplateView.as_view(template_name='user_accounts/password_reset_done.html'), 
         name='password_reset_done'),

    # URL pattern for the password reset confirm view, expects uidb64 and token as parameters
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),

    # URL pattern for the password reset complete view, uses TemplateView to render a static template
    path('reset/done/', 
         TemplateView.as_view(template_name='user_accounts/password_reset_complete.html'), 
         name='password_reset_complete'),
]
