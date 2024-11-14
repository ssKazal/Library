from rest_framework import serializers

from ..models import Author, Book, BookLog


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name", "date_of_birth"]


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), write_only=True
    )

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author_id",
            "author",
            "published_date",
            "genre",
            "is_archived",
        ]
