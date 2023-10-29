from django.db import models
from django.urls import reverse
import uuid

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre')

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    isbn = models.CharField(max_length=13, unique=True, help_text="Enter the 13 digit ISBN number")

    genre = models.ManyToManyField(Genre, help_text="Select the genre's of the book")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-pages', args=[str(self.id)])