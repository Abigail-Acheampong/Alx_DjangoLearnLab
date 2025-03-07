# from django.contrib import admin

# # Register your models here.
# from .models import Book

# admin.site.register(Book) #where Book is the table.


# customization of the admin interface for the Book model.
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

# Unregister first to avoid AlreadyRegistered error
# admin.site.unregister(Book)  # Add this line
admin.site.register(Book, BookAdmin)
