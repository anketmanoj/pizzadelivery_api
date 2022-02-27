from .models import Orders
from rest_framework import serializers


# create OrderCreationSerializer that uses Model Serializer and imports the fields for the Order model
class OrderCreationSerializer(serializers.ModelSerializer):

    size = serializers.CharField(max_length=20)
    order_status = serializers.HiddenField(default='PENDING')
    quantity = serializers.IntegerField()

    class Meta:
        model = Orders
        fields = ['id', 'size', 'order_status', 'quantity']


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('id', 'size', 'order_status', 'quantity')
        depth = 1


class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('order_status',)
