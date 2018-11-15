from rest_framework import serializers

from .models import blogPosts


class BlogPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = blogPosts
        fields = '__all__'