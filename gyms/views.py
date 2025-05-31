from rest_framework import generics
from .models import Gym
from .serializers import GymSerializer

class GymListCreateView(generics.ListCreateAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer

class GymRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer