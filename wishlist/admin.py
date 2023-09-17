from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from .models import Wishlist,WishlistItem

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('wishlist_id', 'date_added')
    search_fields = ('wishlist_id', 'date_added')
    list_filter = ('wishlist_id',)
    list_per_page = 10
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'80'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 80})},
    }

admin.site.register(Wishlist, WishlistAdmin)


admin.site.register(WishlistItem)