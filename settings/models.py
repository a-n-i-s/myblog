from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from user.models import Author
# Create your models here.
class BaseSettings(models.Model):
    class Meta:
      abstract=True
      
    def __str__(self):
        return str(self.__class__.__name__)+'@'+str(self.owner)

    def get_absolute_url(self):
        return reverse(self.__class__.__name__)
    
class UserSetting(BaseSettings):
    owner=models.OneToOneField(get_user_model(),on_delete=models.CASCADE,blank=True,editable=False)
    darkmode=models.BooleanField(default=False)
    showcomments=models.BooleanField(default=True)
class AdminSetting(BaseSettings):
    pass

class AuthorSetting(BaseSettings):
    owner=models.OneToOneField(Author,on_delete=models.CASCADE,blank=True,editable=False)
