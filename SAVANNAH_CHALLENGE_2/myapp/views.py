from rest_framework import generics
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer

class CustomerListCreateView(generics.CustomerListCreateView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderListCreateView(generics.ListCreativeAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer