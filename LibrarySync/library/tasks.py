from celery import shared_task
from .models import Author, Book, BorrowRecord
import os
import json
from datetime import datetime

@shared_task
def generate_report():
    total_authors = Author.objects.count()
    total_books = Book.objects.count()
    total_borrowed_books = BorrowRecord.objects.filter(return_date__isnull=True).count()

    report_data = {
        "total_authors": total_authors,
        "total_books": total_books,
        "total_borrowed_books": total_borrowed_books,
        "generated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    }

    report_dir = os.path.join('reports')
    os.makedirs(report_dir, exist_ok=True)

    filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(os.path.join(report_dir, filename), 'w') as file:
        json.dump(report_data, file)

    return report_data
