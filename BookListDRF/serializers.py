from .models import Book
from rest_framework import serializers

class BookSerializer:
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price']