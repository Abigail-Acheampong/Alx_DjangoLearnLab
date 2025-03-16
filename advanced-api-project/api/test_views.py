from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Book

class BookAPITestCase(APITestCase):
    """
    Test case for Book API endpoints.
    """

    def setUp(self):
        """
        Create test data before running tests.
        """
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create test books
        self.book1 = Book.objects.create(title="Django Basics", author="John Doe", publication_year=2021)
        self.book2 = Book.objects.create(title="Advanced Django", author="Jane Smith", publication_year=2022)

        # API Endpoints
        self.list_create_url = reverse('book-list')  # URL name in urls.py
        self.detail_url = lambda book_id: reverse('book-detail', args=[book_id])

    def test_create_book_authenticated(self):
        """
        Test creating a new book with authentication.
        """
        self.client.login(username='testuser', password='testpassword')

        data = {"title": "New Django Book", "author": "Alex Brown", "publication_year": 2023}
        response = self.client.post(self.list_create_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
