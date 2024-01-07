from django_filters import FilterSet
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
