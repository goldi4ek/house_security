from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLES = (
        ("admin", "Administrator"),
        ("manager", "Manager"),
        ("guard", "Guard"),
    )
    role = models.CharField(max_length=20, choices=ROLES, default="guard")

    def __str__(self):
        return self.username

    def get_assigned_entrance(self):
        from houses.models import Entrance

        return Entrance.objects.filter(guards=self)


class House(models.Model):
    address = models.CharField(max_length=255)
    manager = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="managed_houses",
    )

    def __str__(self):
        return self.address


class Entrance(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name="entrances")
    number = models.PositiveIntegerField()
    guards = models.ManyToManyField(CustomUser, related_name="entrances", blank=True)

    def __str__(self):
        return f"{self.house.address} - Entrance {self.number}"


class Apartment(models.Model):
    entrance = models.ForeignKey(
        Entrance, on_delete=models.CASCADE, related_name="apartments"
    )
    number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.entrance.house.address} - Entrance {self.entrance.number} - Apartment {self.number}"
