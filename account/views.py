from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegisterForm, LoginForm
from baseapp import utils

from .models import LoginHistory


def sign_out(request):
    logout(request)
    return redirect("sign_in")


def sign_up(request):
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Registration successful you can now Sign in")
            return redirect("sign_in")
    else:
        form = RegisterForm()
    return render(request, "auth/register.html", {"form": form})


def sign_in(request):
    destination = utils.get_next_destination(request)
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data["email"], password=form.cleaned_data["password"]
            )
            if user:
                login(request, user)
                LoginHistory.objects.create(
                    user=user, log_ip=utils.get_client_ip(request), city="####"
                )
                if destination:
                    return redirect(f"{destination}")
                else:
                    return redirect("dashboard")
        else:
            messages.warning(request, ("Invalid Username Or Password."))
            return redirect("sign_in")
    else:
        form = LoginForm()
    return render(request, "auth/login.html", {"form": form})
