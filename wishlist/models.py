from django.db import models
from authentication.models import CustomUser
from products.models import Product

# Create your models here.

class Wishlist(models.Model):
    wishlist_id = models.CharField(max_length=250)
    user = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.wishlist_id
    
class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.wishlist.wishlist_id