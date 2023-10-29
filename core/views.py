from datetime import datetime
from django.shortcuts import render
from django.http import Http404
from .models import Book

def index(request):
    context = {"time": datetime.now().strftime("%H:%M:%S")}
    return render(request, "core/index.html", context)

def booklist(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'core/booklist.html', context)

def bookpage(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404('Book was not found')

    context = {'book': book}
    return render(request, 'core/bookpage.html', context)