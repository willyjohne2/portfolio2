"""
URL configuration for portfolio_config project.
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path("", include("portfolio.urls")),
    path("auth/", include("accounts.urls")),
    path("admin/", admin.site.urls),
]

# Serve media files in both development and production (for Render ephemeral storage)
urlpatterns += [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]
