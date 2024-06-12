# models.py

# Import necessary modules from Django
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field

# Define the Post model
class Post(models.Model):
    # ForeignKey field to link a post to a user (author)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # CKEditor5 field for rich text content
    content = CKEditor5Field(config_name='default')
    # DateTime field to store the creation time of the post
    created_at = models.DateTimeField(auto_now_add=True)
    # DateTime field to store the last update time of the post
    updated_at = models.DateTimeField(auto_now=True)
    # DateTime field to store the last edited time of the post
    last_edited_at = models.DateTimeField(null=True, blank=True)

    # Override the save method to update the last_edited_at field
    def save(self, *args, **kwargs):
        if self.pk:  # Check if the post already exists (is being updated)
            self.last_edited_at = timezone.now()
        super().save(*args, **kwargs)

    # String representation of the Post model
    def __str__(self):
        return f"{self.author.username}'s Post"

# Define the Comment model
class Comment(models.Model):
    # ForeignKey field to link a comment to a post
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    # ForeignKey field to link a comment to a user (author)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Text field to store the content of the comment
    content = models.TextField()
    # DateTime field to store the creation time of the comment
    created_at = models.DateTimeField(auto_now_add=True)

    # String representation of the Comment model
    def __str__(self):
        return f"Comment by {self.author.username}"

# Define the Like model
class Like(models.Model):
    # ForeignKey field to link a like to a post
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    # ForeignKey field to link a like to a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # DateTime field to store the creation time of the like
    created_at = models.DateTimeField(auto_now_add=True)

    # Meta class to define unique constraints
    class Meta:
        # Ensure that each user can like a post only once
        unique_together = ('post', 'user')

    # String representation of the Like model
    def __str__(self):
        return f"Like by {self.user.username}"
