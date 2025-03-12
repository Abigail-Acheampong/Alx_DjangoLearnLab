from django.db import models

class Author(models.Model):
    """
    Represents an author in the system.

    Fields:
    - name (CharField): Stores the author's name.
    
    Relationships:
    - One-to-Many: One author can have multiple books.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book in the system.

    Fields:
    - title (CharField): The title of the book.
    - publication_year (IntegerField): The year the book was published.
    - author (ForeignKey): Establishes a One-to-Many relationship with Author.

    Relationships:
    - Each book is linked to a single author.
    - If an author is deleted, all their books are also deleted (`on_delete=models.CASCADE`).
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
