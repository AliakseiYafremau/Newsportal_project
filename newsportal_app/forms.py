from django.core.exceptions import ValidationError

from .profanities import profanity_list
from django import forms
from .models import Post

from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
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


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user
