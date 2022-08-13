from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
class User(AbstractUser):
  def is_author(self):
    return self.author is not None


class Author(models.Model):
  STATUS=[
    
    (0,'normal'),
    (1,'blocked'),
  ]
  user=models.OneToOneField(get_user_model(),on_delete=models.CASCADE,related_name='author')
  name=models.CharField(max_length=200)
  about=models.TextField()
  status=models.IntegerField(choices=STATUS,default=0)
  def get_absolute_url(self):
      return reverse("author_detail", kwargs={"pk": self.pk})
  
  def __str__(self):
    return str(self.user)


class AuthorRequest(models.Model):
  STATUS=[
    
    (0,'normal'),
    (1,'blocked'),
  ]
  user=models.OneToOneField(get_user_model(),on_delete=models.CASCADE,related_name='request')
  name=models.CharField(max_length=200)
  about=models.TextField()
  status=models.IntegerField(choices=STATUS,default=0)
  class Meta:
    pass
  def __str__(self):
    return str(self.user)

  def get_absolute_url(self):
      return reverse("authorrequest_status", kwargs={"pk": self.pk})
  

    
