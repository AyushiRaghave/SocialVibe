# urls.py

# Import the path function from django.urls module to define URL patterns
from django.urls import path
# Import the views module from the current package to link the URL patterns to view functions
from . import views

# Define the URL patterns
urlpatterns = [
    # Home page: '' indicates the root URL, linked to the home view
    path('', views.home, name='home'),
    # Create post page: 'create/' URL, linked to the create_post view
    path('create/', views.create_post, name='create_post'),
    # Post detail page: '<int:post_id>/' URL, linked to the post_detail view
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    # Like post action: '<int:post_id>/like/' URL, linked to the like_post view
    path('<int:post_id>/like/', views.like_post, name='like_post'),
    # Edit post page: '<int:post_id>/edit/' URL, linked to the edit_post view
    path('<int:post_id>/edit/', views.edit_post, name='edit_post'),
    # Delete post action: '<int:post_id>/delete/' URL, linked to the delete_post view
    path('<int:post_id>/delete/', views.delete_post, name='delete_post'),
    # Delete comment action: 'comment/<int:comment_id>/delete/' URL, linked to the delete_comment view
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]
