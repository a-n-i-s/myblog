from django.shortcuts import render
from .serializers import AuthorSerializer, PostSerializer
from .models import Author, Post
from rest_framework import fields, generics, serializers

# Create your views here.

class PostList(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    

class PostDetail(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class AuthorDetail(generics.RetrieveAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

class AuthorList(generics.ListAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

