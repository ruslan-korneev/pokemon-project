from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.profiles.api.serializers import ProfileSerializer


Master = get_user_model()


class MasterRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = ('username', 'password', 'sex', 'age')


class MasterListSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer()

    class Meta:
        model = Master
        fields = ('username', 'sex', 'age', 'profile')
