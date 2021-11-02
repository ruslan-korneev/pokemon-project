from django.db import models

from apps.masters.models import Master


class Inventory(models.Model):
    name = models.CharField(max_length=10, default='Inventory', editable=False)
    max_cells = models.PositiveIntegerField(default=16)

    def __str__(self):
        return f"{self.inventory}'s inventory"

    class Meta:
        db_table = 'inventory'
        verbose_name_plural = 'Inventory'
