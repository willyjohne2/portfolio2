from django.urls import path
from . import views

urlpatterns = [
    # Frontend Pages
    path("", views.index, name="index"),
    path("about/", views.about_view, name="about"),
    path("projects/", views.projects_view, name="projects"),
    path("projects/<int:pk>/", views.project_detail, name="project_detail"),
    path("contact/", views.contact_view, name="contact"),
    path("contact/submit/", views.contact_submit, name="contact_submit"),
    # Admin Dashboard
    path("dashboard/", views.admin_dashboard, name="admin_dashboard"),
    # Projects Management
    path("dashboard/projects/", views.projects_manage, name="projects_manage"),
    path("dashboard/projects/new/", views.project_create, name="project_create"),
    path("dashboard/projects/<int:pk>/edit/", views.project_edit, name="project_edit"),
    path(
        "dashboard/projects/<int:pk>/delete/",
        views.project_delete,
        name="project_delete",
    ),
    # Skills Management
    path("dashboard/skills/", views.skills_manage, name="skills_manage"),
    path("dashboard/skills/new/", views.skill_create, name="skill_create"),
    path("dashboard/skills/<int:pk>/edit/", views.skill_edit, name="skill_edit"),
    path("dashboard/skills/<int:pk>/delete/", views.skill_delete, name="skill_delete"),
    # About Management
    path("dashboard/about/", views.about_manage, name="about_manage"),
    # Messages Management
    path("dashboard/messages/", views.messages_view, name="messages"),
    path("dashboard/messages/<int:pk>/", views.message_detail, name="message_detail"),
    path(
        "dashboard/messages/<int:pk>/delete/",
        views.message_delete,
        name="message_delete",
    ),
    # Reply Management
    path(
        "dashboard/messages/<int:pk>/reply/",
        views.reply_to_message,
        name="reply_message",
    ),
    path("dashboard/reply/<int:pk>/delete/", views.delete_reply, name="delete_reply"),
]
