from rest_framework import serializers
from rest_framework.serializers import Serializer, CharField

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password2'}, write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'avatar', 'phone_number', 'password', 'password2')

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            avatar=validated_data['avatar'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class ChangePasswordSerializer(Serializer):
    model = User

    old_password = CharField(required=True)
    new_password = CharField(required=True)

