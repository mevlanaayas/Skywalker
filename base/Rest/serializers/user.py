# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer, CharField, EmailField, Serializer
from base.models import CustomUser


class UserSerializer(ModelSerializer):
    """

    """
    class Meta:
        """

        """
        model = CustomUser
        fields = '__all__'


class RegisterSerializer(ModelSerializer):
    """

    """
    password = CharField(write_only=True, style={'input_type': 'password'})
    contact = CharField(max_length=100)

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            contact=validated_data['contact'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        """

        """
        model = CustomUser
        fields = ('username', 'email', 'password', 'contact')


class LoginSerializer(Serializer):
    """

    """

    email = EmailField()
    password = CharField(style={'input_type': 'password'})
