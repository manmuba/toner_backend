from django.db import models
from authentication.models import CustomUser
from products.models import Product

# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250)
    user = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def total(self):
        return self.product.price * self.quantity
    
    def __str__(self) -> str:
        return self.cart.cart_id
    