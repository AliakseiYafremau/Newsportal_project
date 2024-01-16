from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.contrib.auth.models import Group


@receiver(user_signed_up)
def user_signed_up_handler(request, user, **kwargs):
    group = Group.objects.get(name='common')

    user.groups.add(group)
