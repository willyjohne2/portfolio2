from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def admin_login(request):
    """Admin login view"""
    if request.user.is_authenticated:
        return redirect("admin_dashboard")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("admin_dashboard")
        else:
            messages.error(request, "Invalid credentials or insufficient permissions.")

    return render(request, "accounts/admin_login.html")


@login_required(login_url="admin_login")
def admin_logout(request):
    """Admin logout view"""
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("index")

@login_required(login_url="admin_login")
@require_http_methods(["GET", "POST"])
def profile_settings(request):
    """View to change username and password"""
    password_form = PasswordChangeForm(request.user)
    
    if request.method == "POST":
        action = request.POST.get("action")
        
        if action == "update_username":
            new_username = request.POST.get("username", "").strip()
            if new_username:
                request.user.username = new_username
                request.user.save()
                messages.success(request, f"Username updated to {new_username} successfully!")
            else:
                messages.error(request, "Username cannot be empty.")
                
        elif action == "update_password":
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Keep the user logged in
                messages.success(request, "Password updated successfully!")
                return redirect("profile_settings")
            else:
                messages.error(request, "Please correct the errors in the password form.")

    return render(request, "accounts/profile_settings.html", {
        "password_form": password_form
    })
