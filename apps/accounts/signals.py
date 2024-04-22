from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.accounts.models import CustomUser
from apps.accounts.services.utils import unique_invitation_code


@receiver(post_save, sender=CustomUser)
def create_user(sender, instance, created, **kwargs):
    if created:
        instance.invitation_code = unique_invitation_code()
        instance.save()
