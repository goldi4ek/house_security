from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class House(models.Model):
    address = models.CharField(max_length=255)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='managed_houses')

    def __str__(self):
        return self.address

class Entrance(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='entrances')
    number = models.PositiveIntegerField()
    guards = models.ManyToManyField(User, related_name='entrances', blank=True)

    def __str__(self):
        return f"{self.house.address} - Entrance {self.number}"

class Apartment(models.Model):
    entrance = models.ForeignKey(Entrance, on_delete=models.CASCADE, related_name='apartments')
    number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.entrance.house.address} - Entrance {self.entrance.number} - Apartment {self.number}"
