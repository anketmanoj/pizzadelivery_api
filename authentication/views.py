from .models import User
from .serializers import UserCreationSerializer
from rest_framework import generics, status
from rest_framework.response import Response

# Create your views here.


class HelloAuthView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={'message': 'Hello, World!'}, status=status.HTTP_200_OK)


class UserCreateView(generics.GenericAPIView):
    serializer_class = UserCreationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
