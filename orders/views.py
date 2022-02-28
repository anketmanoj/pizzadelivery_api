from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import Orders
from .serializers import OrderCreationSerializer, OrderDetailSerializer, OrderStatusUpdateSerializer
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()


class HelloOrderView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={'message': 'Hello, Orders!'}, status=status.HTTP_200_OK)


class OrderCreateListView(generics.GenericAPIView):
    serializer_class = OrderCreationSerializer
    queryset = Orders.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        user = request.user
        orders = Orders.objects.all()
        serializer = OrderCreationSerializer(orders, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderCreationSerializer(data=request.data)
        user = request.user

        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        order = get_object_or_404(Orders, pk=pk)
        serializer = OrderDetailSerializer(order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        order = get_object_or_404(Orders, pk=pk)
        user = request.user
        serializer = OrderDetailSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order = get_object_or_404(Orders, pk=pk)
        order.delete()
        return Response(data={'message': 'Order deleted'}, status=status.HTTP_200_OK)


class UpdateOrderStatus(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        order = get_object_or_404(Orders, pk=pk)
        user = request.user
        serializer = OrderStatusUpdateSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserOrdersView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        orders = Orders.objects.all().filter(customer=user)
        serializer = OrderDetailSerializer(orders, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserOrderDetailView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id, pk):
        user = User.objects.get(pk=user_id)
        order = Orders.objects.all().filter(customer=user).get(pk=pk)
        serializer = OrderDetailSerializer(order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
