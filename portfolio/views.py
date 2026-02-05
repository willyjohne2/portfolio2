from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.http import require_http_methods
from .models import About, Skill, Project, ContactMessage, MessageReply


def index(request):
    """Home page view"""
    about = About.objects.first()
    skills_by_category = {}

    skills = Skill.objects.all()
    for skill in skills:
        category = skill.get_category_display()
        if category not in skills_by_category:
            skills_by_category[category] = []
        skills_by_category[category].append(skill)

    projects = Project.objects.all()[:10]

    context = {
        "about": about,
        "skills_by_category": skills_by_category,
        "projects": projects,
    }
    return render(request, "portfolio/index.html", context)


def about_view(request):
    """About page view"""
    about = About.objects.first()
    skills_by_category = {}

    skills = Skill.objects.all()
    for skill in skills:
        category = skill.get_category_display()
        if category not in skills_by_category:
            skills_by_category[category] = []
        skills_by_category[category].append(skill)

    context = {
        "about": about,
        "skills_by_category": skills_by_category,
    }
    return render(request, "portfolio/about.html", context)


def projects_view(request):
    """Projects page view"""
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "portfolio/projects.html", context)


def project_detail(request, pk):
    """Project detail view"""
    project = get_object_or_404(Project, pk=pk)
    other_projects = Project.objects.exclude(pk=pk)[:3]

    context = {
        "project": project,
        "other_projects": other_projects,
    }
    return render(request, "portfolio/project_detail.html", context)


def contact_view(request):
    """Contact page view"""
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")
        else:
            messages.error(request, "Please fill in all fields.")

    return render(request, "portfolio/contact.html")


def contact_submit(request):
    """AJAX endpoint for contact form submission"""
    if request.method != "POST":
        return JsonResponse({"success": False, "error": "Invalid request method"})

    name = request.POST.get("name", "").strip()
    email = request.POST.get("email", "").strip()
    message = request.POST.get("message", "").strip()

    if not all([name, email, message]):
        return JsonResponse({"success": False, "error": "All fields are required"})

    try:
        ContactMessage.objects.create(name=name, email=email, message=message)
        return JsonResponse(
            {"success": True, "message": "Thank you! Your message has been sent."}
        )
    except Exception as e:
        return JsonResponse(
            {"success": False, "error": "An error occurred. Please try again."}
        )


# ============ DASHBOARD VIEWS ============


@login_required(login_url="admin_login")
def admin_dashboard(request):
    """Admin dashboard home"""
    projects_count = Project.objects.count()
    skills_count = Skill.objects.count()
    messages_count = ContactMessage.objects.filter(is_read=False).count()
    total_messages = ContactMessage.objects.count()

    context = {
        "projects_count": projects_count,
        "skills_count": skills_count,
        "unread_messages": messages_count,
        "total_messages": total_messages,
    }
    return render(request, "dashboard/dashboard.html", context)


# Projects Management
@login_required(login_url="admin_login")
def projects_manage(request):
    """Manage projects"""
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "dashboard/projects_manage.html", context)


@login_required(login_url="admin_login")
def project_create(request):
    """Create new project"""
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()
        long_description = request.POST.get("long_description", "").strip()
        technologies = request.POST.get("technologies", "").strip()
        github_url = request.POST.get("github_url", "").strip()
        live_url = request.POST.get("live_url", "").strip()

        if not all([title, description, technologies]):
            messages.error(request, "Please fill in all required fields.")
            return render(request, "dashboard/project_form.html")

        project = Project(
            title=title,
            description=description,
            long_description=long_description,
            technologies=technologies,
            github_url=github_url or None,
            live_url=live_url or None,
        )

        if "image" in request.FILES:
            project.image = request.FILES["image"]

        project.save()
        messages.success(request, "Project created successfully!")
        return redirect("projects_manage")

    return render(request, "dashboard/project_form.html")


@login_required(login_url="admin_login")
def project_edit(request, pk):
    """Edit existing project"""
    project = get_object_or_404(Project, pk=pk)

    if request.method == "POST":
        project.title = request.POST.get("title", "").strip()
        project.description = request.POST.get("description", "").strip()
        project.long_description = request.POST.get("long_description", "").strip()
        project.technologies = request.POST.get("technologies", "").strip()
        project.github_url = request.POST.get("github_url", "").strip() or None
        project.live_url = request.POST.get("live_url", "").strip() or None

        if not all([project.title, project.description, project.technologies]):
            messages.error(request, "Please fill in all required fields.")
            return render(request, "dashboard/project_form.html", {"project": project})

        if "image" in request.FILES:
            project.image = request.FILES["image"]

        project.save()
        messages.success(request, "Project updated successfully!")
        return redirect("projects_manage")

    return render(request, "dashboard/project_form.html", {"project": project})


@login_required(login_url="admin_login")
def project_delete(request, pk):
    """Delete project"""
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    messages.success(request, "Project deleted successfully!")
    return redirect("projects_manage")


# Skills Management
@login_required(login_url="admin_login")
def skills_manage(request):
    """Manage skills"""
    skills = Skill.objects.all()
    context = {"skills": skills}
    return render(request, "dashboard/skills_manage.html", context)


@login_required(login_url="admin_login")
def skill_create(request):
    """Create new skill"""
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        category = request.POST.get("category", "").strip()
        proficiency = request.POST.get("proficiency", 50)

        if not all([name, category]):
            messages.error(request, "Please fill in all required fields.")
            return render(
                request,
                "dashboard/skill_form.html",
                {"categories": Skill._meta.get_field("category").choices},
            )

        Skill.objects.create(name=name, category=category, proficiency=int(proficiency))
        messages.success(request, "Skill created successfully!")
        return redirect("skills_manage")

    context = {"categories": Skill._meta.get_field("category").choices}
    return render(request, "dashboard/skill_form.html", context)


@login_required(login_url="admin_login")
def skill_edit(request, pk):
    """Edit existing skill"""
    skill = get_object_or_404(Skill, pk=pk)

    if request.method == "POST":
        skill.name = request.POST.get("name", "").strip()
        skill.category = request.POST.get("category", "").strip()
        skill.proficiency = int(request.POST.get("proficiency", 50))

        if not all([skill.name, skill.category]):
            messages.error(request, "Please fill in all required fields.")
            return render(
                request,
                "dashboard/skill_form.html",
                {
                    "skill": skill,
                    "categories": Skill._meta.get_field("category").choices,
                },
            )

        skill.save()
        messages.success(request, "Skill updated successfully!")
        return redirect("skills_manage")

    context = {"skill": skill, "categories": Skill._meta.get_field("category").choices}
    return render(request, "dashboard/skill_form.html", context)


@login_required(login_url="admin_login")
def skill_delete(request, pk):
    """Delete skill"""
    skill = get_object_or_404(Skill, pk=pk)
    skill.delete()
    messages.success(request, "Skill deleted successfully!")
    return redirect("skills_manage")


# About Management
@login_required(login_url="admin_login")
def about_manage(request):
    """Manage about section"""
    about = About.objects.first()

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        role = request.POST.get("role", "").strip()
        institution = request.POST.get("institution", "").strip()
        bio = request.POST.get("bio", "").strip()
        interests = request.POST.get("interests", "").strip()
        experience_level = request.POST.get("experience_level", "").strip()

        if not about:
            about = About()

        about.name = name
        about.role = role
        about.institution = institution
        about.bio = bio
        about.interests = interests
        about.experience_level = experience_level

        if "profile_image" in request.FILES:
            about.profile_image = request.FILES["profile_image"]

        about.save()
        messages.success(request, "About section updated successfully!")
        return redirect("about_manage")

    context = {"about": about}
    return render(request, "dashboard/about_manage.html", context)


# Messages Management
@login_required(login_url="admin_login")
def messages_view(request):
    """View all contact messages"""
    all_messages = ContactMessage.objects.all()
    unread_count = ContactMessage.objects.filter(is_read=False).count()

    context = {
        "messages": all_messages,
        "unread_count": unread_count,
    }
    return render(request, "dashboard/messages.html", context)


@login_required(login_url="admin_login")
def message_detail(request, pk):
    """View single message"""
    message = get_object_or_404(ContactMessage, pk=pk)
    message.is_read = True
    message.save()

    context = {"message": message}
    return render(request, "dashboard/message_detail.html", context)


@login_required(login_url="admin_login")
def message_delete(request, pk):
    """Delete message"""
    message = get_object_or_404(ContactMessage, pk=pk)
    message.delete()
    messages.success(request, "Message deleted successfully!")
    return redirect("messages")


# Message Reply Management
@login_required(login_url="admin_login")
def reply_to_message(request, pk):
    """Reply to a contact message"""
    from django.core.mail import send_mail
    from django.conf import settings

    message = get_object_or_404(ContactMessage, pk=pk)

    if request.method == "POST":
        reply_text = request.POST.get("reply_text", "").strip()

        if reply_text:
            # Create or update reply
            reply, created = MessageReply.objects.update_or_create(
                message=message, defaults={"reply_text": reply_text}
            )

            # Send email to the contact message sender
            try:
                email_subject = "Re: Your Message from Wilson Maina"
                email_body = f"""Hello {message.name},

Thank you for reaching out! Here's my reply to your message:

---
YOUR MESSAGE:
{message.message}

---
MY REPLY:
{reply_text}

---

If you have any further questions, feel free to contact me again.

Best regards,
Wilson Maina
Software Engineering Student
Kirinyaga University"""

                send_mail(
                    subject=email_subject,
                    message=email_body,
                    from_email=settings.ADMIN_REPLY_EMAIL,
                    recipient_list=[message.email],
                    fail_silently=False,
                )
                messages.success(
                    request, "Reply sent successfully and email delivered!"
                )
            except Exception as e:
                messages.warning(
                    request, f"Reply saved but email failed to send: {str(e)}"
                )

            return redirect("message_detail", pk=pk)
        else:
            messages.error(request, "Reply cannot be empty.")

    context = {"message": message}
    return render(request, "dashboard/reply_message.html", context)


@login_required(login_url="admin_login")
def delete_reply(request, pk):
    """Delete a reply"""
    from .models import MessageReply

    reply = get_object_or_404(MessageReply, pk=pk)
    message_id = reply.message.id
    reply.delete()
    messages.success(request, "Reply deleted successfully!")
    return redirect("message_detail", pk=message_id)
