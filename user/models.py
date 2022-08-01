from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
class User(AbstractUser):
  pass


class Author(models.Model):
  STATUS=[
    
    (0,'normal'),
    (1,'blocked'),
  ]
  user=models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
  name=models.CharField(max_length=200)
  about=models.TextField()
  status=models.IntegerField(choices=STATUS,default=0)

  def __str__(self):
    return str(self.user)