from .models import BaseRegisterForm
from django.views.generic import CreateView
from django.contrib.auth.models import User


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/newspaper'
