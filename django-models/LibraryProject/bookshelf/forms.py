from django import forms
from .models import Book  # Import your model

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']  # Define the fields you need
        