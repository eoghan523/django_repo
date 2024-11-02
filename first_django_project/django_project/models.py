from django.db import models
from django.utils import timezone
from datetime import timedelta

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()

    def full_name(self):
        """Returns the full name of the author."""
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Book(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def is_recent(self):
        """Checks if the book was published in the last 10 years."""
        return self.published_date >= timezone.now().date() - timedelta(days=365 * 10)

    def __str__(self):
        return self.title
