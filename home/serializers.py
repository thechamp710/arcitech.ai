from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'blog_text']  # Exclude 'user' since it's set in the view
        read_only_fields = ['user']  # Make 'user' read-only since it's set in the view

    def create(self, validated_data):
        # Fetch user from request context
        user = self.context['request'].user

        # Create Blog instance with validated data and assign user
        blog = Blog.objects.create(user=user, **validated_data)
        return blog