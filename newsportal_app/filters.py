import django_filters
from django_filters import FilterSet

from django import forms
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'text': ['icontains'],
            'rating': ['gt'],
            'date_of_creation': [
                'lt',
                'gt',
            ],
        }


class PostSearchFilter(FilterSet):
    text = django_filters.CharFilter(lookup_expr='icontains')
    author__user__username = django_filters.CharFilter(lookup_expr='icontains')
    date_of_creation = django_filters.DateTimeFilter(widget=forms.DateTimeInput(attrs={'type': 'date'}))
