from rest_framework import serializers
from .models import Order, About, Faq, Partners, Terms


class OrderSerializer(serializers.ModelSerializer):
    order_status=serializers.HiddenField(default="PENDING")
    size=serializers.CharField(max_length=25)
    quantity=serializers.IntegerField()
    flavour=serializers.CharField(max_length=40)

    class Meta:
        model=Order 
        fields=['order_status', 'size', 'quantity','flavour']


class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    order_status = serializers.CharField(max_length=25)

    class Meta:
        model=Order
        fields=['order_status']

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model=About 
        fields=['title', 'body', 'Author', 'created_on', 'updated_at']

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model=Faq 
        fields=['title', 'body', 'Author', 'created_on', 'updated_at']

class TermsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Terms 
        fields=['title', 'body', 'Author', 'created_on', 'updated_at']

class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Partners 
        fields=['title', 'body', 'Author', 'created_on', 'updated_at', 'picture']