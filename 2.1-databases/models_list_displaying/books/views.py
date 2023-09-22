from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
import datetime

from books.models import Book


def books_view(request):
    books_objects = Book.objects.all()
    template = 'books/books_list.html'
    context = {
        'list_book': books_objects
    }
    return render(request, template, context)

def book_date(request, pub_date):


    template = 'books/books_date.html'

    books_objects = Book.objects.filter(pub_date=pub_date)
    books_next = (Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first())
    books_previous = Book.objects.filter(pub_date__lt=pub_date).order_by('pub_date').first()
    books_next_1 = books_next
    books_previous_1 = books_previous
    if books_next:
        books_next = str(books_next.pub_date)
        books_next_1 = str(f'books/{books_next}')
    else:
        books_next = None
    if books_previous:
        books_previous = str(books_previous.pub_date)
        books_previous_1 = str(f'books/{books_previous}')
    else:
        books_previous = None
    context = {
        'books': books_objects,
        'next_book': books_next,
        'next_book_1': books_next_1,
        'previous_book_1': books_previous_1,
        'previous_book': books_previous,
    }

    return render(request, template, context)
