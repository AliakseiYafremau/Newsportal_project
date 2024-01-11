import django_filters
from django_filters import FilterSet

from django import forms
from .models import Post


class PostFilter(FilterSet):
    date_of_creation = django_filters.DateTimeFilter(field_name='date_of_creation', widget=forms.DateTimeInput(attrs={'type': 'date'}), lookup_expr='date')
    date_of_creation__gt = django_filters.DateTimeFilter(field_name='date_of_creation', widget=forms.DateTimeInput(attrs={'type': 'date'}), lookup_expr='date__gt')
    date_of_creation__lt = django_filters.DateTimeFilter(field_name='date_of_creation', widget=forms.DateTimeInput(attrs={'type': 'date'}), lookup_expr='date__lt')

    class Meta:
        model = Post
        fields = {
            'text': ['icontains'],
            'rating': ['gt'],
        }


class PostSearchFilter(FilterSet):
    text = django_filters.CharFilter(lookup_expr='icontains')
    author__user__username = django_filters.CharFilter(lookup_expr='icontains')
    date_of_creation = django_filters.DateTimeFilter(widget=forms.DateTimeInput(attrs={'type': 'date'}), lookup_expr='date')
