from django.shortcuts import render


def index(request):
    return render(request, "users/dashboard.html")


def withdraw(request):
    return render(request, "users/withdrawal.html")


def transactions_(request):
    return render(request, "users/transactions.html")
