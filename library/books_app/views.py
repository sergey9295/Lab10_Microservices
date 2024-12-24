from django.shortcuts import render
from rest_framework import viewsets

from .models import Book, BookCategory, Author
from .serializers import BookSerializer, BookCategorySerializer, AuthorSerializer


# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    """
    В представлениях беспечивается обработка всех CRUD запросов 
    благодаря использованию класса ModelViewSet фреймворка DRF
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCategoryViewSet(viewsets.ModelViewSet):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
