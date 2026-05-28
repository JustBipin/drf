from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import CustomUser
from .serializers import CustomUserSerializer
from .permissions import IsAdminOrSelfOrReadOnly


class UserViewSet(ModelViewSet):
    """
    create and list users for blog api
    """

    permission_classes = [IsAdminOrSelfOrReadOnly]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
