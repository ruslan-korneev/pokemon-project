from rest_framework import serializers
from apps.inventory.api.serializers import InventorySerializer

from apps.profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    inventory = InventorySerializer()

    class Meta:
        model = Profile
        fields = ('level', 'balance', 'inventory')