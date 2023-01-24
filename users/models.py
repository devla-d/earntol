from django.db import models


from account.models import Account


class Bank(models.Model):
    acc_name = models.CharField(max_length=50, blank=True, null=True)
    acc_num = models.CharField(max_length=50, blank=True, null=True)
    ty_pe = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.ty_pe} "


class Transactions(models.Model):
    user = models.ForeignKey(
        Account,
        related_name="user_transactions",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    amount = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    approved_date = models.DateTimeField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    status = models.CharField(max_length=40, default="pending")
    trans_type = models.CharField(max_length=50)

    bank_details = models.ForeignKey(
        Bank, related_name="trans_bank", on_delete=models.CASCADE, blank=True, null=True
    )

    unique_u = models.CharField(max_length=30, blank=True, null=True, unique=True)

    def __str__(self):
        return f"{self.user.username} :  {self.trans_type}"


STATUS = (
    ("active", "active"),
    ("inactive", "inactive"),
    ("pending", "pending"),
    ("completed", "completed"),
)
