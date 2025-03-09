from django.shortcuts import render
from rest_framework import generics
from .models import Book  # Import from the current app (api)
from .serializers import BookSerializer
from rest_framework import viewsets #for crud operations

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for performing CRUD operations on the Book model.
    """
    queryset = Book.objects.all()  # Query all books
    serializer_class = BookSerializer  # Use the BookSerializer