from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from users.models import User


_UNSAVED_AVATAR = 'unsaved_avatar'


@receiver(pre_save, sender=User)
def skip_saving_file(sender, instance, **kwargs):
    if not instance.pk and not hasattr(instance, _UNSAVED_AVATAR):
        setattr(instance, _UNSAVED_AVATAR, instance.avatar)
        instance.avatar = None


@receiver(post_save, sender=User)
def save_file(sender, instance, created, **kwargs):
    if created and hasattr(instance, _UNSAVED_AVATAR):
        instance.avatar = getattr(instance, _UNSAVED_AVATAR)
        instance.save()
        instance.__dict__.pop(_UNSAVED_AVATAR)
