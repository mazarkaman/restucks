from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from rest_framework.settings import api_settings
from users.serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    """to register user"""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class CreateTokeUserView(ObtainAuthToken):
    """to login user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    permission_classes = [AllowAny]

