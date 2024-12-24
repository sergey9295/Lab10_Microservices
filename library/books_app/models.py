from django.db import models


class BookCategory(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField(max_length=64, unique=True)

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    category = models.ForeignKey(
        BookCategory,
        on_delete=models.SET_NULL,
        related_name="book",
        null=True,
        blank=True,
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="book",
    )

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title
