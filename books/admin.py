from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'quantity_page', 'created_at')
    search_fields = ('title', 'author')

