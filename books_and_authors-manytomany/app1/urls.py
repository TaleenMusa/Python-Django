from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addbook', views.addbook),
    path('books/<int:id>', views.bookdetails),
    path('authortobook/<int:id>', views.authortobook),
    path('authors', views.authors),
    path('addauthor', views.addauthor),
    path('authors/<int:id>', views.showauthors),
    path('booktoauthor/<int:id>', views.booktoauthor),
]
