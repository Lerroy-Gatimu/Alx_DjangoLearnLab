from LibraryProject.relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="J.K. Rowling")
books_by_author = Book.objects.filter(author=author)
print("Books by author:", books_by_author)

# List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print("Books in library:", books_in_library)

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("Librarian for the library:", librarian)
