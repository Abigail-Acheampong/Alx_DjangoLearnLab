from rest_framework import serializers
from datetime import date
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.

    Serializes all fields of the Book model.
    Includes validation to ensure the publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Custom validation to ensure the publication_year is not greater than the current year.
        Prevents users from setting publication dates in the future.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.

    Fields:
    - name: The author's name.
    - books: A nested representation of related books (using BookSerializer).

    Relationship Handling:
    - Uses `BookSerializer` with `many=True` to serialize all books written by the author.
    - The `books` field is set to `read_only=True` to prevent book creation through this serializer.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
