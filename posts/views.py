from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .serializers import PostSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

