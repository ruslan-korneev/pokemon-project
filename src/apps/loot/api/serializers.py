from rest_framework import serializers

from apps.loot.models import PokeballInventory


class PokeballInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PokeballInventory
        fields = ('pokeball', 'quantity')