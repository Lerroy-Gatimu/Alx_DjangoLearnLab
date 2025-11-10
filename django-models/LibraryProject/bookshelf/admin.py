from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for easier navigation
    list_filter = ('publication_year', 'author')
    
    # Enable search by title and author
    search_fields = ('title', 'author')
