from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
from .models import Library

# Implementing the function-based view for listing books and their authors
def list_books(request):
    books = Book.objects.all()  # Query all books
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Implementing class based view for displaying the details of a specific library.
class LibraryDetailView(DetailView):
    """Class-based view to display details of a specific library."""
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"