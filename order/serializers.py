from rest_framework import serializers
from .models import Order, OrderItem, OrderTrack

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    many = True
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTrack
        fields = '__all__'