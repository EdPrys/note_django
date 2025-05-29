from django.urls import path
from .views import NoteListAPIView, NoteCreateAPIView, NoteDetailAPIView

urlpatterns = [
    path('api/notes/', NoteListAPIView.as_view(), name='note-list'),
    path('api/notes/create/', NoteCreateAPIView.as_view(), name='note-create'),

    path('api/notes/<int:pk>/', NoteDetailAPIView.as_view(), name='note-detail')
]