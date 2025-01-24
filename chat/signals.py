from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .models import Profile

@receiver(user_logged_in)
def set_online(sender, request, user, **kwargs):
    Profile.objects.update_or_create(user=user, defaults={'is_online': True})

@receiver(user_logged_out)
def set_offline(sender, request, user, **kwargs):
    Profile.objects.update_or_create(user=user, defaults={'is_online': False})
