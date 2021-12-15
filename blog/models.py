from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    title=models.CharField(name='title',max_length=255,blank=False)
    publishtime=models.DateTimeField(name='last_updated',auto_now=True)
    author=models.ForeignKey('Author',on_delete=models.CASCADE)
    body=models.TextField(name='body',blank=False,max_length=10000,default='empty')
    hits=models.IntegerField(default=0,editable=False,null=False)
    coverimg=models.ImageField(name='cover_image',null=True,blank=True)
    
    def __str__(self):
        return self.title
        
    def sort_description(self):
    	return self.body[:30]+"..."

    
class Author(models.Model):
    name=models.CharField(name='name',max_length=255,blank=False)
    detail=models.TextField(name='description',blank=False,max_length=10000,default='empty')
    image=models.ImageField(name='profile_picture',null=True,blank=True)
    
    def __str__(self):
        return self.name
     
    def post_count(self):
    	return self.post_set.count()   
     	
    def get_absolute_url(self):
    	pass
     	
class Comment(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE)
    detail=models.CharField(name='detail',max_length=255,blank=False)
    time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)+": "+str(self.detail)[:30]
