from django.shortcuts import render


def index(request):
    return render(request, "users/dashboard.html")


def withdraw(request):
    return render(request, "users/withdrawal.html")


def transactions_(request):
    return render(request, "users/transactions.html")


def settings(request):
    return render(request, "users/settings.html")


def change_password(request):
    return render(request, "users/change-password.html")
