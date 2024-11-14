from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, null=True)
    date_of_birth = models.DateField(null=True)

    def __srt__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255, null=True)
    author = models.ForeignKey(
        Author, related_name="books", null=True, on_delete=models.CASCADE
    )
    published_date = models.DateField(null=True)
    genre = models.DateField(max_length=100, null=True)
    is_archived = models.BooleanField(default=False)

    def __srt__(self):
        return self.title
    
class BookLog(models.Model):
    book_title = models.CharField(max_length=255, null=True)
    author_name = models.CharField(max_length=100, null=True, 
    )
    action = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __srt__(self):
        return self.title
    
