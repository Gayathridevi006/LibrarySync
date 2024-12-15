from django.urls import path
from .views import (
    AuthorListCreateView, AuthorDetailView, 
    BookListCreateView, BookDetailView, 
    BorrowRecordListCreateView, ReportView
)

urlpatterns = [
    # Authors
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),

    # Books
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Borrow Records
    path('borrow-records/', BorrowRecordListCreateView.as_view(), name='borrow-record-list-create'),

    # Reports
    path('reports/', ReportView.as_view(), name='report'),
]



