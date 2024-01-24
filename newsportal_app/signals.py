from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .utils import send_notifications

from newsportal_app.models import PostCategory


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    print(sender)
    print(instance)
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers = []
        for category in categories:
            subscribers += category.subscribers.all()

        send_notifications(instance.text[:50], instance.pk, instance.title, subscribers)
