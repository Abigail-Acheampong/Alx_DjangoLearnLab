from django.db import models

# The Author model represents a book author with a unique name.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# The Book model represents a book with a title, publication year, 
# and a foreign key linking it to an Author.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
