from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.models import LoginHistory
from .models import *
from baseapp import utils
from .forms import UserUpdateForm, PasswordChangeForm


@login_required()
def index(request):
    user = request.user
    context = {
        "logs": LoginHistory.objects.filter(user=user).order_by("-date")[:3],
    }

    return render(request, "users/dashboard.html", context)


@login_required()
def withdraw(request):
    user = request.user
    if request.POST:
        accountnum = request.POST.get("accountnum")
        accountname = request.POST.get("accountname")
        bank = request.POST.get("bank")
        amount = int(request.POST.get("amount"))

        if user.balance >= amount:
            bank = Bank.objects.create(
                acc_name=accountname, acc_num=accountnum, ty_pe=bank
            )
            transaction = Transactions.objects.create(
                user=user,
                amount=amount,
                trans_type=utils.W,
                unique_u=utils.trans_code(),
            )
            transaction.bank_details = bank
            user.balance -= amount
            user.save()
            transaction.save()
            messages.success(request, ("Withdrawal Placed !"))
            return redirect("withdraw")
        else:
            messages.warning(request, ("Insufficient Funds!"))
            return redirect("withdraw")

    return render(request, "users/withdrawal.html")


@login_required()
def transactions_(request):
    transactions = Transactions.objects.filter(user=request.user).order_by("-date")
    return render(request, "users/transactions.html", {"transactions": transactions})


@login_required()
def settings(request):
    user = request.user
    if request.POST:
        p_form = PasswordChangeForm(request.POST, instance=user)
        if p_form.is_valid():
            password1 = p_form.cleaned_data["password1"]
            user.set_password(password1)
            user.save()
            messages.success(request, f"Password Change")
            return redirect("settings")
    else:
        p_form = PasswordChangeForm(initial={"user_id": user.id})
    return render(request, "users/change-password.html", {"p_form": p_form})


# def change_password(request):
#     return render(request, "users/change-password.html")
