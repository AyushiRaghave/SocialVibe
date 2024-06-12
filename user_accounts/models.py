# Import necessary modules from Django
from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

# Define the Profile model which extends the User model with additional fields
class Profile(models.Model):
    # One-to-one relationship with the built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Optional bio field for the user's profile
    bio = models.TextField(blank=True, null=True)
    
    # Optional profile picture field, images will be uploaded to 'profile_pictures/' directory
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    
    # Field to check if the user's email is verified
    email_verified = models.BooleanField(default=False)
    
    # Field to store the email verification token
    verification_token = models.CharField(max_length=64, blank=True, null=True)

    # Method to generate a random verification token and save it to the model
    def generate_verification_token(self):
        self.verification_token = get_random_string(64)  # Generate a random string of 64 characters
        self.save()  # Save the updated token to the database

    # String representation of the Profile model
    def __str__(self):
        return self.user.username  # Return the username of the associated user
