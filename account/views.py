from django.shortcuts import render


def sign_up(request):
    return render(request, "auth/register.html")


def sign_in(request):
    return render(request, "auth/login.html")
