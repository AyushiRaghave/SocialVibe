# forms.py

# Import necessary modules from Django
from django import forms

# Import the Post and Comment models from the current app's models
from .models import Post, Comment

# Import the CKEditor5 widget to use it in the form fields
from django_ckeditor_5.widgets import CKEditor5Widget


# Define the form class for creating and updating posts
class PostForm(forms.ModelForm):
    # Use the CKEditor5 widget for the 'content' field with the default configuration
    content = forms.CharField(widget=CKEditor5Widget(config_name='default'), required=False)

    # Meta class to specify the model and fields to include in the form
    class Meta:
        # Specify the model to be used with this form
        model = Post
        # Specify the fields to be included in the form
        fields = ['content']


# Define the form class for creating and updating comments
class CommentForm(forms.ModelForm):
    # Meta class to specify the model and fields to include in the form
    class Meta:
        # Specify the model to be used with this form
        model = Comment
        # Specify the fields to be included in the form
        fields = ['content']
