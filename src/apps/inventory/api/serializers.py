from rest_framework import serializers

from apps.inventory.models import Inventory
from apps.loot.api.serializers import PokeballInventorySerializer


class InventorySerializer(serializers.ModelSerializer):

    pokeballs = PokeballInventorySerializer(many=True)

    class Meta:
        model = Inventory
        fields = ('max_cells', 'pokeballs')
