from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(ModelViewSet):
    """
    ViewSets for viewing and editing Post Viewsets
    """

    permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.id)


# class PostList(ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthorOrAdminOrReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
