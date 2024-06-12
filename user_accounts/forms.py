# Import necessary modules and classes from Django
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm
)
from .models import Profile

# Define a custom form for user registration by extending UserCreationForm
class UserRegisterForm(UserCreationForm):
    # Add an email field with custom widget styling
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg'}))

    class Meta:
        model = User  # Use the built-in User model
        fields = ['username', 'email', 'password1', 'password2']  # Specify the fields to be included in the form
        widgets = {  # Apply custom styling to the fields
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
        }

# Define a custom form for updating user information by extending ModelForm
class UserUpdateForm(forms.ModelForm):
    # Add an email field with custom widget styling
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg'}))

    class Meta:
        model = User  # Use the built-in User model
        fields = ['username', 'email']  # Specify the fields to be included in the form
        widgets = {  # Apply custom styling to the fields
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        }

# Define a custom form for updating profile information by extending ModelForm
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile  # Use the custom Profile model
        fields = ['bio', 'profile_picture']  # Specify the fields to be included in the form
        widgets = {  # Apply custom styling to the fields
            'bio': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
        }

# Define a custom form for changing password by extending PasswordChangeForm
class CustomPasswordChangeForm(PasswordChangeForm):
    # Add old password, new password, and confirm new password fields with custom widget styling
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})
    )

    class Meta:
        model = User  # Use the built-in User model
        fields = ['old_password', 'new_password1', 'new_password2']  # Specify the fields to be included in the form

# Define a custom form for resetting password by extending PasswordResetForm
class CustomPasswordResetForm(PasswordResetForm):
    # Add an email field with custom widget styling
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg'}))

    class Meta:
        model = User  # Use the built-in User model
        fields = ['email']  # Specify the fields to be included in the form

# Define a custom form for setting a new password by extending SetPasswordForm
class CustomSetPasswordForm(SetPasswordForm):
    # Add new password and confirm new password fields with custom widget styling
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})
    )

    class Meta:
        model = User  # Use the built-in User model
        fields = ['new_password1', 'new_password2']  # Specify the fields to be included in the form
