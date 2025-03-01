from bookshelf.models import Book

# Retrieve the book with title "Nineteen Eighty-Four"
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Try to retrieve all books to confirm deletion
all_books = Book.objects.all()
print("Remaining Books:", list(all_books))

# Output
Remaining Books: []