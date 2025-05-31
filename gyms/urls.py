from django.urls import path
from .views import GymListCreateView, GymRetrieveUpdateDestroyView

urlpatterns = [
    path('', GymListCreateView.as_view(), name='gym-list-create'),
    path('<int:pk>/', GymRetrieveUpdateDestroyView.as_view(), name='gym-detail'),
]