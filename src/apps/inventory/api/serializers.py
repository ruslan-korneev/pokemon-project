from rest_framework import serializers

from apps.inventory.models import Inventory
from apps.loot.api.serializers import PokeballInventorySerializer


class InventorySerializer(serializers.ModelSerializer):

    pokeballs = serializers.RelatedField(source='pokeballs.name')

    class Meta:
        model = Inventory
        fields = ('max_cells', 'pokeballs')