from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import blogPosts
from .serializers import BlogPostSerializers

# Create your views here.
class DefaultsMixin(object):
    """Default Settings for view"""
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class BlogPostViewSet(viewsets.ModelViewSet):
    """ API Endpoint for listing and creating bank and its rates"""
    queryset = blogPosts.objects.all()
    serializer_class = BlogPostSerializers



