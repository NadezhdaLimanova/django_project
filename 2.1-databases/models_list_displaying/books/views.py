from django.shortcuts import render
from books.models import Book

def books_view(request):
    books = Book.objects.all()
    template = 'books/books_list.html'
    context = {'books': books}
    return render(request, template, context)


def book_detail(request, pub_date):
    books = Book.objects.filter(pub_date=pub_date)
    next_book = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
    if next_book:
        next_book = str(next_book.pub_date)
    else:
        next_book = None
    previous_book = Book.objects.filter(pub_date__lt=pub_date).order_by('pub_date').last()
    if previous_book:
        previous_book = str(previous_book.pub_date)
    else:
        previous_book = None
    template = 'books/book.html'
    context = {
        'books': books,
        'next_book': next_book,
        'previous_book': previous_book
               }
    return render(request, template, context)

