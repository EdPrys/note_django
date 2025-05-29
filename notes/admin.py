from django.contrib import admin
from .models import Note, Tag

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_important', 'created_at')
    list_filter = ('is_important', 'created_at')
    search_fields = ('title', 'content')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)