from django.shortcuts import render, redirect
from . models import *


def index(request):
    context = {
        'allbooks': Book.objects.all(),
    }
    return render(request, "index.html", context)


def addbook(request):
    Book.objects.create(
        title=request.POST['title'], description=request.POST['description'])
    return redirect('/')


def bookdetails(request, id):
    context = {
        'onebook': Book.objects.get(id=int(id)),
        'allauthors': Author.objects.all(),
    }
    return render(request, "detail.html", context)


def authortobook(request, id):
    author1 = Author.objects.get(id=request.POST['author'])
    book1 = Book.objects.get(id=int(id))
    book1.authors.add(author1)
    return redirect('/books/' + str(id))


def authors(request):
    context = {
        'allauthors': Author.objects.all(),
    }
    return render(request, "author.html", context)


def addauthor(request):
    Author.objects.create(
        first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect('/authors')


def showauthors(request, id):
    context = {
        'allbooks': Book.objects.all,
        'author': Author.objects.get(id=int(id)),
    }
    return render(request, 'detailauthor.html', context)


def booktoauthor(request, id):
    author1 = Author.objects.get(id=id)
    book1 = Book.objects.get(id=request.POST['book'])
    author1.books.add(book1)
    return redirect('/authors/' + str(id))
