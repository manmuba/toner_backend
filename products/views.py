from rest_framework import generics, filters, pagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter

class ProductListCreateRetrieveView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ['name', 'price', 'created_at']  # Fields to sort by
    ordering = ['-created_at']  # Default ordering
    pagination_class = pagination.PageNumberPagination  # Use PageNumberPagination

    def get(self, request, *args, **kwargs):
        # Check if a detail view is requested (e.g., /products/<pk>/)
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return super().list(request, *args, **kwargs)
