from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrAdminOrReadOnly


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrAdminOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
