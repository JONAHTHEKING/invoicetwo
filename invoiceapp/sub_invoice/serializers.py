from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            name=validated_data["name"],
            email=validated_data["email"],
           
        )
        return user

class ItemSerializer(serializers.ModelSerializer):
        class Meta:
                model=Items
                fields="__all__"

class InvoicesSerializer(serializers.ModelSerializer):
    items=ItemSerializer(many=True, read_only=True)

    class Meta:
        model=Invoices
        fields="__all__"    


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)

        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid username or password !!")
        