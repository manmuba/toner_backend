from django.shortcuts import render
from rest_framework import generics, pagination, status
from rest_framework.response import Response

from .models import Order,OrderItem
from .serializers import  OrderSerializer, OrderItemSerializer

# Create your views here.

