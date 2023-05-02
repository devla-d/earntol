from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Account
from baseapp import utils


@receiver(post_save, sender=Account)
def create_referral(sender, instance, created, **kwargs):
    if created:

        utils.send_regMail(instance)
