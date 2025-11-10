from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    output = "<h1>Books Available:</h1><ul>"
    for book in books:
        output += f"<li>{book.title} by {book.author.name}</li>"
    output += "</ul>"
    return HttpResponse(output)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

