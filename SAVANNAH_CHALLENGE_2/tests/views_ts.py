# tests/test_views.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer

class CustomerAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_customer_creation(self):
        response = self.client.post(reverse('customer-list'), {'name': 'Andrew Kamau'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_customer_retrieval(self):
        customer = Customer.objects.create(name='Andrew Kamau')
        response = self.client.get(reverse('customer-detail', args=[customer.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Andrew Kamau')

    
class OrderAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_order_creation(self):
        response = self.client.post(reverse('order-list'), {'item': 'Product A', 'amount': 100})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_order_retrieval(self):
        order = Order.objects.create(item='Product B', amount=150)
        response = self.client.get(reverse('order-detail', args=[order.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['item'], 'Product B')

    
