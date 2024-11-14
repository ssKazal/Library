from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Book, BookLog


@receiver(post_save, sender=Book)
def log_book_creation(sender, instance, created, **kwargs):
    if created:
        BookLog.objects.create(
            action="create", book_title=instance.title, author_name=instance.author.name
        )


@receiver(post_delete, sender=Book)
def log_book_deletion(sender, instance, created, **kwargs):
    if created:
        BookLog.objects.create(
            action="delete", book_title=instance.title, author_name=instance.author.name
        )
