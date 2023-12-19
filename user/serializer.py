from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name','user_email','user_number','user_password','is_verify')


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_email','password')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['is_verify']