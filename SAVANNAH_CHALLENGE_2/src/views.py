from rest_framework import generics
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from social_django.utils import psa
from africastalking.SMS import SMSError, SMS

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @psa('social:complete', 'openid_connect')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @psa('social:complete', 'openid_connect')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @psa('social:complete', 'openid_connect')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def perform_create(self, serializer):
        
        instance = super().perform_create(serializer)

       
        try:
            username = '' # africastalking username
            api_key = '' # africastalking api key
            sender = '' # sms senders name
            message = f"New Order Alert: Order #{instance.id} has been added."

            sms = SMS(username, api_key)
            response = sms.send(message, [instance.customer.phone_number], sender)

           
            if response['SMSMessageData']['Recipients'][0]['status'] == 'Success':
                print("SMS alert sent successfully.")
            else:
                print(f"Failed to send SMS alert. Response: {response}")

        except SMSError as e:
            print(f"Error sending SMS alert: {e}")

        return instance

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @psa('social:complete', 'openid_connect')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
