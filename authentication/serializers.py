from rest_framework import serializers
from .models import User
from phonenumber_field.serializerfields import PhoneNumberField


# create a user serializer class that takes model serializer
class UserCreationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    username = serializers.CharField(max_length=255)
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'phone_number', 'password']

    def validate(self, attrs):
        username_exists = User.objects.filter(
            username=attrs['username']).exists()

        if username_exists:
            raise serializers.ValidationError(
                'Username already exists')

        email_exists = User.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise serializers.ValidationError("Email already exists")

        phone_number_exists = User.objects.filter(
            phone_number=attrs['phone_number']).exists()

        if phone_number_exists:
            raise serializers.ValidationError("Phone number already exists")

        return super().validate(attrs)
