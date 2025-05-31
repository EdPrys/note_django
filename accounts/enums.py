from django.db import models

class Role(models.TextChoices):
    PLAYER = 'player', 'Гравець'
    MODERATOR = 'moderator', 'Модератор'