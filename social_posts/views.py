# views.py for social_posts

# Import necessary modules from Django
from django.shortcuts import render, redirect, get_object_or_404  # Utility functions for view handling
from django.contrib.auth.decorators import login_required  # Decorator to ensure views are accessed by authenticated users
from django.contrib import messages  # For displaying success/error messages
from .models import Post, Comment, Like  # Import the Post, Comment, and Like models
from .forms import PostForm, CommentForm  # Import forms for creating and editing posts and comments
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseForbidden  # For handling different types of HTTP responses

@login_required
def like_post(request, post_id):
    # Retrieve the post object or return a 404 error if not found
    post = get_object_or_404(Post, id=post_id)
    try:
        # Check if the user has already liked the post
        like = Like.objects.get(post=post, user=request.user)
        like.delete()  # Remove the like if it exists
        liked = False
    except Like.DoesNotExist:
        # Create a like if it doesn't exist
        Like.objects.create(post=post, user=request.user)
        liked = True

    # Get the current like count
    likes_count = post.likes.count()

    # If the request is AJAX, return a JSON response
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'liked': liked, 'likes_count': likes_count})

    # Redirect to the post detail page if not AJAX
    return redirect('post_detail', post_id=post_id)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)  # Create a form instance with POST data
        if form.is_valid():
            post = form.save(commit=False)  # Save the form without committing to the database
            post.author = request.user  # Set the author of the post to the current user
            post.save()  # Save the post
            messages.success(request, 'Your post has been created!')  # Display success message
            return redirect('home')  # Redirect to the home page
    else:
        form = PostForm()  # Create an empty form instance
    return render(request, 'social_posts/create_post.html', {'form': form})

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Retrieve the post or return a 404 error
    comments = post.comments.all()  # Get all comments related to the post
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)  # Create a form instance with POST data
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)  # Save the form without committing to the database
            comment.post = post  # Associate the comment with the post
            comment.author = request.user  # Set the author of the comment to the current user
            comment.save()  # Save the comment
            messages.success(request, 'Your comment has been added!')  # Display success message
            return redirect('post_detail', post_id=post_id)  # Redirect to the post detail page
    else:
        comment_form = CommentForm()  # Create an empty form instance
    user_has_liked = post.likes.filter(user=request.user).exists()  # Check if the user has liked the post
    return render(request, 'social_posts/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form, 'user_has_liked': user_has_liked})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Retrieve the post or return a 404 error
    if request.user != post.author:
        return HttpResponseBadRequest("You are not authorized to edit this post.")  # Return an error if the user is not the author
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)  # Create a form instance with POST data and the existing post
        if form.is_valid():
            form.save()  # Save the updated post
            messages.success(request, 'Your post has been updated!')  # Display success message
            return redirect('post_detail', post_id=post_id)  # Redirect to the post detail page
    else:
        form = PostForm(instance=post)  # Create a form instance with the existing post
    return render(request, 'social_posts/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Retrieve the post or return a 404 error
    if request.user != post.author:
        return HttpResponseBadRequest("You are not authorized to delete this post.")  # Return an error if the user is not the author
    if request.method == 'POST':
        post.delete()  # Delete the post
        messages.success(request, 'Your post has been deleted!')  # Display success message
        return redirect('home')  # Redirect to the home page
    return render(request, 'social_posts/delete_post.html', {'post': post})

@login_required
def home(request):
    posts = Post.objects.all().order_by('-created_at')  # Get all posts ordered by creation date (newest first)
    user_likes = {post.id: post.likes.filter(user=request.user).exists() for post in posts} if request.user.is_authenticated else {}  # Check if the user has liked each post
    return render(request, 'social_posts/home.html', {'posts': posts, 'user_likes': user_likes})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)  # Retrieve the comment or return a 404 error
    if request.user != comment.author:
        return HttpResponseForbidden("You are not authorized to delete this comment.")  # Return an error if the user is not the author
    if request.method == 'POST':
        comment.delete()  # Delete the comment
        messages.success(request, 'Your comment has been deleted!')  # Display success message
        return redirect('post_detail', post_id=comment.post.id)  # Redirect to the post detail page
