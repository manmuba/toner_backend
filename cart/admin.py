from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from .models import Cart,CartItem

class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')
    search_fields = ('cart_id', 'date_added')
    list_filter = ('cart_id',)
    list_per_page = 10
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'80'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 80})},
    }

admin.site.register(Cart, CartAdmin)


admin.site.register(CartItem)
