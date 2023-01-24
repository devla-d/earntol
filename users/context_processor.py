# from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site


def dashboard_processor(request):
    current_site = get_current_site(request)
    context = {}
    context["domain"] = current_site.domain
    return context
