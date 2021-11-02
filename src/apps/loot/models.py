from django.db import models

from apps.inventory.models import Inventory


class Potion(models.Model):
    name = models.CharField(max_length=256)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'potions'
        ordering = ('price',)


class PotionInventory(models.Model):
    potion = models.ForeignKey(Potion, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.potion} - {self.quantity}"

    class Meta:
        db_table = 'potions_inventory'
        verbose_name = "Potion's Inventory"
        verbose_name_plural = "Potion's Inventory"


class Pokeball(models.Model):
    name = models.CharField(max_length=256)
    level = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'pokeball'


class PokeballInventory(models.Model):
    pokeball = models.ForeignKey(Pokeball, on_delete=models.CASCADE, related_name='pokeball')
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='pokeballs')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.pokeball} - {self.quantity}"

    class Meta:
        db_table = 'pokeballs_inventory'
        verbose_name = "Pokeball's Inventory"
        verbose_name_plural = "Pokeball's Inventory"
