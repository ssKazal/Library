from library.celery import app
from datetime import timedelta
from django.utils import timezone
from app.models import Book


@app.task(bind=True, default_retry_delay=1 * 60)
def archive_old_books():
    ten_years_ago = timezone.now().date() - timedelta(days=365 * 10)
    Book.objects.filter(published_date__lt=ten_years_ago).update(is_archived=True)
