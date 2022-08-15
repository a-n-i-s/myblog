from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from .models import UserSetting,AuthorSetting
from user.models import Author
@receiver(post_save,sender=get_user_model())
def create_usersetting(sender,created,instance,**kwargs):
  if created:
      UserSetting.objects.create(owner=instance)

@receiver(post_save,sender=Author)
def create_authorsetting(sender,created,instance,**kwargs):
  if created:
      AuthorSetting.objects.create(owner=instance)
