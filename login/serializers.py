from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


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

    class Meta:
        model = User
        fields = ['password', 'password']


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']
