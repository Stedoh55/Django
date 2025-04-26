from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.

class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)           # A comma ',' just before ')' is essential to avoid a TypeError for BasePermissionClass
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)            # A comma ',' just before ')' is essential to avoid a TypeError for BasePermissionClass
    queryset = Post.objects.all()
    serializer_class = PostSerializer
