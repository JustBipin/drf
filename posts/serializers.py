from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Post


class PostSerializer(ModelSerializer):
    author = ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = ["id", "author", "title", "body", "created_at"]
