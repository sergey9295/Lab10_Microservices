from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookCategoryViewSet, BookViewSet, AuthorViewSet


router = DefaultRouter()
router.register(r'book_category', BookCategoryViewSet, basename='book_category')
router.register(r'book', BookViewSet, basename='book')
router.register(r'author', AuthorViewSet, basename='author')

urlpatterns = [
    path('', include(router.urls))
]
