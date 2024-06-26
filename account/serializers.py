from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password as django_validate_password


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField()
    pincode = serializers.CharField()

    def validate(self, data):
        # Validate username uniqueness
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError('Username is already taken')

        # Validate password complexity
        try:
            django_validate_password(data['password'])
        except ValidationError as e:
            raise serializers.ValidationError(str(e))

        # Validate phone number (must be 10 digits)
        if len(data['phone_number']) != 10 or not data['phone_number'].isdigit():
            raise serializers.ValidationError('Phone number must be 10 digits long and contain only numbers.')

        # Validate pincode (must be 6 digits)
        if len(data['pincode']) != 6 or not data['pincode'].isdigit():
            raise serializers.ValidationError('Pincode must be 6 digits long and contain only numbers.')

        return data

    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'].lower()
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError('Invalid credentials')
        else:
            raise serializers.ValidationError('Must include "username" and "password"')

        data['user'] = user
        return data

    def get_jwt_token(self, validated_data):
        user = validated_data['user']
        refresh = RefreshToken.for_user(user)
        return {
            'message': 'Login successful',
            'data': {
                'token': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            }
        }
