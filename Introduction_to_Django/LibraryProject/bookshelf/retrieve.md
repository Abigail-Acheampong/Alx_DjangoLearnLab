# Retrieve a book

book = Book.objects.get(id=3)

# Display all attributes

print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")

# Output

Title: 1984
Author: Goerge Orwell
Publication Year: 1949
