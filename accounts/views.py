from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
