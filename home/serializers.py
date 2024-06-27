# serializers.py
from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'user', 'title', 'blog_text']
        read_only_fields = ['user']

    def create(self, validated_data):
        user = self.context['request'].user
        blog = Blog.objects.create(user=user, **validated_data)
        return blog
