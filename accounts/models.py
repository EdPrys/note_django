from django.db import models
from django.conf import settings
from .enums import Role

class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.PLAYER)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"