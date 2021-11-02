from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.masters.models import Master

from .signals import get_starting_loot


class Profile(models.Model):
    ''' Instance of masters with stats'''
    user = models.OneToOneField(Master, on_delete=models.CASCADE, related_name='profile')
    inventory = models.OneToOneField('inventory.Inventory', models.PROTECT, related_name='inventory')
    level = models.PositiveIntegerField(default=1)
    balance = models.PositiveIntegerField(default=30000)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'profiles'


@receiver(post_save, sender=Master)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile()
        get_starting_loot(sender, instance, profile)

