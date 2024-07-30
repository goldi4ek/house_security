from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('admin', 'Administrator'),
        ('manager', 'Manager'),
        ('guard', 'Guard'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='guard')

    def __str__(self):
        return self.username

    def get_assigned_entrance(self):
        from houses.models import Entrance
        return Entrance.objects.filter(guards=self)
