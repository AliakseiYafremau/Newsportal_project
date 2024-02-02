from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .tasks import send_notifications

from newsportal_app.models import PostCategory


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    """ Сигнал фиксирующий создание поста """
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers = []
        for category in categories:
            subscribers.extend(category.subscribers.all().values_list("pk", flat=True))

        send_notifications.delay(instance.text[:50], instance.pk, instance.title, subscribers)
