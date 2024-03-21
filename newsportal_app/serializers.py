from rest_framework import serializers
from newsportal_app.models import Author, Post


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user', 'rating']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'type', 'date_of_creation', 'category', 'title', 'text', 'rating']
