# Retrieve the book with title "1984"
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
updated_book = Book.objects.get(id=book.id)
print(f"Updated Title: {updated_book.title}")

# Output
Updated Title: Nineteen Eighty-Four