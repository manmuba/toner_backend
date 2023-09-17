from rest_framework import generics, pagination
from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartSerializer
from category.views import IsAdminOrReadOnly

class CartListCreateRetrieveView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    pagination_class = pagination.PageNumberPagination  

class CartItemListCreateRetrieveView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    pagination_class = pagination.PageNumberPagination  
    
class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer