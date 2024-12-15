from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from celery.result import AsyncResult
from .models import Author, Book, BorrowRecord
from .serializers import AuthorSerializer, BookSerializer, BorrowRecordSerializer
from .tasks import generate_report
import os
import json

from django.shortcuts import render

def homepage_view(request):
    return render(request, 'home.html')  # Replace with the desired template

# Author Views
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# Book Views
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Borrow Record Views
class BorrowRecordListCreateView(generics.ListCreateAPIView):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer

# Report Generation
class ReportView(APIView):
    def post(self, request):
        task = generate_report.delay()
        return Response({"message": "Report generation started", "task_id": task.id})

    def get(self, request):
        report_dir = os.path.join('reports')
        if not os.path.exists(report_dir):
            return Response({"error": "No reports found"}, status=404)

        latest_file = max(
            [os.path.join(report_dir, f) for f in os.listdir(report_dir)],
            key=os.path.getctime,
        )
        with open(latest_file, 'r') as file:
            report_data = json.load(file)

        return Response(report_data)
