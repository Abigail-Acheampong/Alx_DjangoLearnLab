from rest_framework import serializers
from .models import Book  # Correct import for the same app


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields of the Book model
