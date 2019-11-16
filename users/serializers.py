"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Purpose: in this serializers module we create serializer classes 
author:  Sachin Shrikant Jadhav
since :  25-09-2019
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    """

    here we creating serializers for user registration

    """
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data["username"],
                                        validated_data["email"],
                                        validated_data["password"])
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class PasswordSerializer(serializers.ModelSerializer):
    """ here we taking username and password"""
    password = serializers.CharField(min_length=8, write_only=True)
    confirm_password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['password', 'confirm_password']


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['image', 'time_stamp']


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserRegisterSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField('get_user_token')
    provider = serializers.CharField(min_length=5, max_length=20)
    access_token = serializers.CharField(max_length=250)
    access_token_secret = serializers.CharField(max_length=200)

    def get_user_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj.user)
        return token.key

    class Meta:
        model = User
        fields = ['username', 'email', 'token', 'provider', 'access_token', 'access_token_secret']
