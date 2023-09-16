from rest_framework import generics, filters, pagination
from .models import Category
from .serializers import CategorySerializer

class CategoryListCreateDetailView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]   
    search_fields = ['name', 'description']  # Fields to search
    ordering_fields = ['name', 'created_at']  # Fields to sort by
    pagination_class = pagination.PageNumberPagination  # Use PageNumberPagination

    def get(self, request, *args, **kwargs):
        # Check if a detail view is requested (e.g., /categories/<pk>/)
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return super().list(request, *args, **kwargs)

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer