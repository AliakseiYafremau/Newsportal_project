from django.core.exceptions import ValidationError

from .profanities import profanity_list
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'type',
            'category',
            'title',
            'text',
        ]

    def clean(self):
        cleaned_data = super().clean()

        text = cleaned_data.get("text")
        title = cleaned_data.get("title")
        for word in profanity_list:
            if word in title:
                raise ValidationError({
                    "title": "Title has profanities"
                })
            if word in text:
                raise ValidationError({
                    "text": "Text has profanities"
                })

        return cleaned_data
