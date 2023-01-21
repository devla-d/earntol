from django.shortcuts import render


def homepage(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def pricing(request):
    return render(request, "pricing.html")


def support(request):
    return render(request, "support.html")
