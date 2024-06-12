# Import necessary modules from Django and other libraries
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .forms import (UserRegisterForm, UserUpdateForm, ProfileUpdateForm, 
                    CustomPasswordChangeForm, CustomPasswordResetForm, CustomSetPasswordForm)
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls import reverse, reverse_lazy
from .models import Profile
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.contrib.auth import get_user_model

# Get the user model
User = get_user_model()

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            profile.generate_verification_token()
            verification_link = request.build_absolute_uri(reverse('verify_email', args=[profile.verification_token]))

            html_message = render_to_string('user_accounts/verification_email.html', {'user': user, 'verification_link': verification_link})
            plain_message = strip_tags(html_message)
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = user.email

            email = EmailMultiAlternatives(
                'Verify your email',
                plain_message,
                from_email,
                [to_email]
            )
            email.attach_alternative(html_message, "text/html")
            email.send()

            messages.success(request, 'Your account has been created! Please verify your email.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user_accounts/register.html', {'form': form})

# Email verification view
def verify_email(request, token):
    try:
        profile = Profile.objects.get(verification_token=token)
        profile.email_verified = True
        profile.verification_token = None
        profile.save()
        messages.success(request, 'Your email has been verified! You can now log in.')
        return redirect('login')
    except Profile.DoesNotExist:
        messages.error(request, 'Invalid verification token!')
        return redirect('register')

# User login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                profile = Profile.objects.get(user=user)
                if profile.email_verified:
                    login(request, user)
                    messages.info(request, f'You are now logged in as {username}.')
                    return redirect('home')  # Redirect to the home page after login
                else:
                    messages.error(request, 'Please verify your email address before logging in.')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    form = AuthenticationForm()
    return render(request, 'user_accounts/login.html', {'form': form})

# User profile deletion view
@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Your profile has been deleted successfully.')
        return redirect('register')
    return render(request, 'user_accounts/delete_profile.html')

# User profile update view
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'user_accounts/profile.html', context)

# User logout view
@login_required
def user_logout(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('login')

# Change password view
@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to update session hash to keep user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'user_accounts/change_password.html', {'form': form})

# Password reset request view
def password_reset_request(request):
    if request.method == 'POST':
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(email=data)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "user_accounts/password_reset_email.html"
                    context = {
                        "email": user.email,
                        'domain': request.META['HTTP_HOST'],
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    html_message = render_to_string(email_template_name, context)
                    plain_message = strip_tags(html_message)
                    from_email = settings.DEFAULT_FROM_EMAIL

                    email = EmailMultiAlternatives(
                        subject,
                        plain_message,
                        from_email,
                        [user.email]
                    )
                    email.attach_alternative(html_message, "text/html")
                    email.send()

                    messages.success(request, "A message with reset password instructions has been sent to your inbox.")
                    return redirect("password_reset_done")
            else:
                messages.error(request, "No user is associated with this email address.")
    password_reset_form = PasswordResetForm()
    return render(request, 'user_accounts/password_reset.html', {'form': password_reset_form})

# Password reset confirm view
def password_reset_confirm(request, uidb64=None, token=None):
    assert uidb64 is not None and token is not None  # Ensure parameters are not None
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)

    if default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been set. You may log in now.")
                return redirect('password_reset_complete')
        else:
            form = SetPasswordForm(user)
    else:
        messages.error(request, 'The reset link is invalid or has expired.')
        return redirect('password_reset')

    return render(request, 'user_accounts/password_reset_confirm.html', {'form': form})
