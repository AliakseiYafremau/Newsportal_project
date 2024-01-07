from django import template
from ..profanities import profanity_list

register = template.Library()


@register.filter()
def censor(text):
    for first in range(len(text)):
        for second in range(1, len(text)+1):
            if text[first:second + 1] in profanity_list:
                text = text[:first + 1] + '*' * (second - first) + text[second + 1:]
    return text
