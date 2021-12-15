from rest_framework import fields
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer 
from .models import Author,Post,Comment


class PostSerializer(HyperlinkedModelSerializer):
    authorname=serializers.ReadOnlyField(source='author.name')
    class Meta:
        model=Post
        fields=['url','title','last_updated','author','authorname','sort_description','body','hits','cover_image']

class AuthorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model=Author
        fields=['url','name']