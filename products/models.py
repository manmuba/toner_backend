from django.db import models
from category.models import Category  # Import Category model if not already imported

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/')
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    on_stock = models.PositiveIntegerField(default=0)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
