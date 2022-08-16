from .models import Favourite
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

@receiver(post_save,sender=get_user_model())
def create_favourite(sender,created,instance,**kwargs):
  if created:
      Favourite.objects.create(owner=instance)
