from ..models import Author, Book, BookLog
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import viewsets, filters


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.select_related("author").all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["author__name", "genre"]
    ordering_fields = ["published_date"]

    def get_queryset(self):
        queryset = super().get_queryset()
        published_date_from = self.request.query_params.get("published_date_from")
        published_date_to = self.request.query_params.get("published_date_to")

        # Range filtering
        if published_date_from and published_date_to:
            queryset = queryset.filter(
                published_date__range=[published_date_from, published_date_to]
            )

        return queryset
