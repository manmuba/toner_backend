from rest_framework import generics, filters, pagination
from .models import Category
from .serializers import CategorySerializer

from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff

class CategoryListCreateDetailView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]   
    search_fields = ['name', 'description']  # Fields to search
    ordering_fields = ['name', 'created_at']  # Fields to sort by
    pagination_class = pagination.PageNumberPagination  # Use PageNumberPagination


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]