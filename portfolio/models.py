from django.db import models
from django.utils import timezone


class About(models.Model):
    """Model for About section content"""

    name = models.CharField(max_length=200, default="Wilson Maina Njuguna")
    role = models.CharField(max_length=200, default="Software Engineering Student")
    institution = models.CharField(max_length=200, default="Kirinyaga University")
    bio = models.TextField(
        default="Second-year Software Engineering Student passionate about web development and cybersecurity."
    )
    interests = models.TextField(default="Web Development, Cybersecurity")
    experience_level = models.CharField(max_length=100, default="Beginner-Intermediate")
    profile_image = models.ImageField(upload_to="profile/", null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "About"


class Skill(models.Model):
    """Model for Skills"""

    SKILL_CATEGORIES = [
        ("language", "Programming Language"),
        ("framework", "Framework"),
        ("tool", "Tool"),
        ("database", "Database"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES)
    proficiency = models.IntegerField(
        default=50, help_text="Proficiency level from 1-100"
    )
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Project(models.Model):
    """Model for Portfolio Projects"""

    title = models.CharField(max_length=200)
    description = models.TextField()
    long_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="projects/")
    technologies = models.CharField(
        max_length=500, help_text="Comma-separated list of technologies"
    )
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    """Model for Contact Form Messages"""

    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Message from {self.name} ({self.email})"


class MessageReply(models.Model):
    """Model for Admin Replies to Contact Messages"""

    message = models.OneToOneField(
        ContactMessage, on_delete=models.CASCADE, related_name="reply"
    )
    reply_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Reply to {self.message.name}"
