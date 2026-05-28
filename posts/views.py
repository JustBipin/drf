from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .models import Post
from .serializers import PostSerializer
from .permissions import IsAdminOrAuthorOrReadOnly


class PostViewSet(ModelViewSet):
    """
    ViewSets for viewing and editing Post Viewsets
    """

    permission_classes = [IsAdminOrAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class PostList(ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthorOrAdminOrReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
