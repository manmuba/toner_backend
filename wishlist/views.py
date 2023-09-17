from rest_framework import generics, pagination, status
from .models import Wishlist, WishlistItem
from .serializers import WishlistItemSerializer
from products.models import Product
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.utils.crypto import get_random_string

class WishlistItemListCreateRetrieveView(generics.ListCreateAPIView):
    serializer_class = WishlistItemSerializer
    pagination_class = pagination.PageNumberPagination
    permission_classes = [AllowAny]

    def get_wishlist(self):
        session_key = self.request.session.session_key

        if not session_key:
            session_key = get_random_string(32)
            self.request.session.create()
            self.request.session.save()

        try:
            wishlist = Wishlist.objects.get(wishlist_id=session_key)
        except Wishlist.DoesNotExist:
            wishlist = Wishlist.objects.create(wishlist_id=session_key)

        return wishlist

    def get_queryset(self):
        wishlist = self.get_wishlist()
        wishlist_items = WishlistItem.objects.filter(wishlist=wishlist)
        return wishlist_items

    def post(self, request, *args, **kwargs):
        wishlist = self.get_wishlist()

        product = Product.objects.get(pk=request.data.get('product'))

        try:
            wishlist_item = WishlistItem.objects.get(wishlist=wishlist, product=product)
            return Response({"response": "Already in wishlist"})
        except WishlistItem.DoesNotExist:
            wishlist_item = WishlistItem.objects.create(
                wishlist=wishlist,
                product=product
            )

        return Response(self.serializer_class(wishlist_item).data, status=status.HTTP_201_CREATED)
# class CartItemListCreateRetrieveView(generics.ListCreateAPIView):
#     serializer_class = CartItemSerializer
#     pagination_class = pagination.PageNumberPagination
#     permission_classes = [AllowAny]

#     def get_queryset(self):
#         try:
#             cart = Cart.objects.get(cart_id=self.request.session.session_key)
#         except Cart.DoesNotExist:
#             cart = Cart.objects.create(cart_id=self.request.session.session_key)
#         cart_items = CartItem.objects.filter(cart=cart)
#         return cart_items

#     def post(self, request, *args, **kwargs):
#         try:
#             cart = Cart.objects.get(cart_id=self.request.session.session_key)
#         except Cart.DoesNotExist:
#             cart = Cart.objects.create(cart_id=self.request.session.session_key)

#         product = Product.objects.get(pk=self.request.data.get('product'))
#         quantity = int(self.request.data.get('quantity'))

#         try:
#             cart_item = CartItem.objects.get(cart=cart, product=product)
#             cart_item.quantity += quantity
#             cart_item.save()
#         except CartItem.DoesNotExist:
#             cart_item = CartItem.objects.create(
#                 quantity=quantity,
#                 cart=cart,
#                 product=product
#             )

#         return Response(self.serializer_class(cart_item).data, status=status.HTTP_201_CREATED)
    
class WishlistItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WishlistItemSerializer
    def get_queryset(self):
        try:
            wishlist = Wishlist.objects.get(wishlist_id=self.request.session.session_key)
            wishlist_items=WishlistItem.objects.filter(wishlist=wishlist)
            return wishlist_items
        except:
            wishlist = Wishlist.objects.create(wishlist_id=self.request.session.session_key)
            wishlist_items=WishlistItem.objects.filter(wishlist=wishlist)
            return wishlist_items