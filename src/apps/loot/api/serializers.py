from rest_framework import serializers

from apps.loot.models import Pokeball, PokeballInventory


class PokeballSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokeball
        fields = '__all__'


class PokeballInventorySerializer(serializers.ModelSerializer):
    
    pokeball = PokeballSerializer()

    class Meta:
        model = PokeballInventory
        fields = ('pokeball', 'quantity')
