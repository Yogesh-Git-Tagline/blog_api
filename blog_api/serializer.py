from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Blog
        fields = ['id', 'title', 'author', 'content', 'created_at']
