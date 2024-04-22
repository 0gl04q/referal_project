from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.accounts.services.validators import phone_regex


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150)
    phone = models.CharField(max_length=12, validators=[phone_regex], unique=True)
    verification_code = models.CharField(max_length=4, null=True, blank=True)
    invitation_code = models.CharField(max_length=6, unique=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ('phone',)
        indexes = [models.Index(fields=['phone', 'verification_code'])]

    def __str__(self):
        return self.phone

    def check_invite(self):
        return InvitationCodeUsers.objects.filter(invite_user=self).exists()


class InvitationCodeUsers(models.Model):
    main_user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='main')
    invite_user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='invite')

    class Meta:
        ordering = ('main_user', 'invite_user')
        unique_together = ('main_user', 'invite_user')
        indexes = [
            models.Index(fields=['main_user']),
            models.Index(fields=['invite_user']),
        ]
