from django.urls import path, include
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
from django.contrib import admin

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # List all books and create a new book
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # Create a new book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve a specific book
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),  # Update a specific book
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),  # Delete a specific book
    path('books/', BookListView.as_view(), name='book-list'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the api.urls for API endpoints
]