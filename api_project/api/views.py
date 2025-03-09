from django.shortcuts import render
from rest_framework import generics
from .models import Book  # Import from the current app (api)
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

