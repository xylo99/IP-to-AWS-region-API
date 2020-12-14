from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name', 'region')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user_with_ip_to_aws_region(**data)
