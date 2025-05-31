# events/models.py

from django.db import models
from django.conf import settings
from gyms.models import Gym
from django.utils import timezone



class Event(models.Model):
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, related_name='events')
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateTimeField()
    max_players = models.PositiveIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} at {self.gym.name} on {self.date.strftime('%Y-%m-%d %H:%M')}"


class Participation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'user')

    def __str__(self):
        return f"{self.user.username} -> {self.event.name} ({'Confirmed' if self.confirmed else 'Pending'})"
