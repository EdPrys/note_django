from rest_framework import serializers

from gyms.models import Gym
from gyms.serializers import GymSerializer
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    gym = serializers.PrimaryKeyRelatedField(queryset=Gym.objects.all())

    class Meta:
        model = Event
        fields = '__all__'