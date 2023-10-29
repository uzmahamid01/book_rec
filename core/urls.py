from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('books', views.booklist, name='booklist'),
    path('book/<int:book_id>', views.bookpage, name='book-pages'),
]
