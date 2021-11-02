from django.contrib import admin

from .models import Inventory
from apps.profiles.admin import ProfileInline


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    inlines = (ProfileInline,)