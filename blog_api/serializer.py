from rest_framework import serializers
from .models import Blog
from django.contrib.auth.models import User


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(source='author.username')
    # author = serializers.SlugRelatedField(
    #     slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Blog
        fields = ['id', 'title', 'author', 'content', 'created_at']
