from .models import About


def about_context(request):
    return {"site_about": About.objects.first()}
