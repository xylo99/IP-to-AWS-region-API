from rest_framework import generics

from user.user_serializer import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer