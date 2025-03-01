import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    """Query all books written by a specific author."""
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)  # ✅ Uses filter()
        return books
    except Author.DoesNotExist:
        return f"No author found with name {author_name}"

def get_books_in_library(library_name):
    """List all books available in a specific library."""
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return f"No library found with name {library_name}"

def get_librarian_for_library(library_name):
    """Retrieve the librarian assigned to a specific library."""
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)  # ✅ Uses .get(library=library)
        return librarian
    except Library.DoesNotExist:
        return f"No library found with name {library_name}"
    except Librarian.DoesNotExist:
        return f"No librarian assigned to {library_name}"

if __name__ == "__main__":
    # Replace with actual names in your database
    author_name = "J.K. Rowling"
    library_name = "Central Library"

    print(f"Books by {author_name}:")
    print(list(get_books_by_author(author_name)))

    print(f"\nBooks in {library_name}:")
    print(list(get_books_in_library(library_name)))

    print(f"\nLibrarian for {library_name}:")
    print(get_librarian_for_library(library_name))