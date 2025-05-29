from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Note
from .serializers import NoteSerializer
from rest_framework import filters

class NoteListAPIView(ListAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['is_important', 'tags']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'is_important']

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

class NoteCreateAPIView(CreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NoteDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)