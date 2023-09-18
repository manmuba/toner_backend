from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from .models import Order, OrderItem, OrderTrack

class OrderAdmin(admin.ModelAdmin):
    list_display = ('display_user_emails', 'order_id', 'status', 'order_date')
    search_fields = ( 'user__email', 'order_id', 'status', 'order_date')
    list_filter = ('user__email', 'order_id', 'status', 'order_date')
    list_per_page = 10
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'80'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 80})},
    }

    def display_user_emails(self, obj):
        return obj.user.email

    display_user_emails.short_description = 'User Emails'

class OrderTrackAdmin(admin.ModelAdmin):
    list_display = ('display_order_id', 'display_user_emails', 'order_process', 'order_shipped', 'out_of_delivery', 'delivered')
    search_fields = ( 'order__order_id', 'order__user__email', 'order_process', 'order_shipped', 'out_of_delivery', 'delivered')
    list_filter = ('order__order_id', 'order__user__email', 'order_process', 'order_shipped', 'out_of_delivery', 'delivered')
    list_per_page = 10
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'80'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 80})},
    }

    def display_order_id(self, obj):
        return obj.order.order_id\
        
    def display_user_emails(self, obj):
        return obj.order.user.email

    display_user_emails.short_description = 'User Emails'

    display_order_id.short_description = 'Order ID'

admin.site.register(Order, OrderAdmin)


admin.site.register(OrderItem)

admin.site.register(OrderTrack, OrderTrackAdmin)