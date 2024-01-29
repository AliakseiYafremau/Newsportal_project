from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from datetime import date, timedelta

from newsportal_app.models import Post, Category
from newsportal_project import settings