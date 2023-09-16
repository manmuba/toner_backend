from rest_framework import generics, filters, pagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter
from category.views import IsAdminOrReadOnly

class ProductListCreateRetrieveView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ['name', 'price', 'created_at']  # Fields to sort by
    ordering = ['-created_at']  # Default ordering
    pagination_class = pagination.PageNumberPagination  # Use PageNumberPagination
    permission_classes = [IsAdminOrReadOnly]

    
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]