from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    zipcode = models.CharField(max_length=30, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    fullname = models.CharField(max_length=100, blank=True, null=True)

    address = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)

    city = models.CharField(max_length=100, blank=True, null=True)

    date_of_birth = models.CharField(max_length=100, blank=True, null=True)

    phone = models.CharField(max_length=30, blank=True, null=True, unique=True)
    balance = models.IntegerField(default=0, blank=True, null=True)
    deposit_balance = models.IntegerField(default=0, blank=True, null=True)
    vip_reward = models.IntegerField(default=0, blank=True, null=True)

    total_withdraw = models.IntegerField(default=0, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


class LoginHistory(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="log_user")
    log_ip = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.log_ip}"
