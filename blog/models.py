from os import O_WRONLY
from django.db import models
from user.models import Author
from django.urls import reverse
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
# Create your models here.

class Post(models.Model):
  PRIVACY=[
    (0,'public'),
    (1,'readers only'),
  ]
  
  title=models.CharField(max_length=200)
  body=models.TextField()
  created_at=models.DateTimeField(auto_now_add=True,verbose_name='time created')
  updated_at=models.DateTimeField(auto_now=True,verbose_name='last updated')
  author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='posts')
  hits=models.IntegerField(default=0,editable=False,verbose_name='view count')
  privacy=models.IntegerField(choices=PRIVACY,default=0)
  tags=TaggableManager(blank=True)
  catagory=models.ForeignKey('Catagory',on_delete=models.CASCADE,related_name='posts')
  def __str__(self):
      return self.title

  
  def get_short_description(self):
    return self.body[:20]+("..." if len(self.body)>20 else "")

  def get_tags(self):
    return self.tags.all()
  def get_comments(self):
    return self.comments.filter(parent=None)

  def get_absolute_url(self):
    return reverse("post_detail", kwargs={"pk": self.pk}) or  ''



'''class Tag(models.Model):

    name=models.CharField(max_length=100)

    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Tag_detail", kwargs={"pk": self.pk})
'''
class Catagory(models.Model):
    parent=models.ForeignKey('self',null=True,blank=True,default=None,on_delete=models.CASCADE,related_name='children')
    name=models.CharField(max_length=100)

    
    
    class Meta:
        verbose_name = "Catagory"
        verbose_name_plural = "Catagories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Catagory_detail", kwargs={"pk": self.pk})
    @property
    def itemcount(self):
        c=self.posts.count()
        for i in self.children.all():
            c+=i.itemcount

        return c


class Comment(models.Model):
    owner=models.ForeignKey(get_user_model(),blank=True,on_delete=models.CASCADE,verbose_name='Commented by')
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    parent=models.ForeignKey('self',default=None,null=True,blank=True,on_delete=models.CASCADE,verbose_name='Reply to',related_name='children')
    body=models.TextField(verbose_name='')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='time created')
    updated_at=models.DateTimeField(auto_now=True,verbose_name='last updated')
  

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.body[:10]+'...'

    def get_absolute_url(self):
        return reverse("comment_detail", kwargs={"pk": self.pk})

class Favourite(models.Model):
    owner=models.OneToOneField(get_user_model(),on_delete=models.CASCADE,related_name='favourites',editable=False)
    posts=models.ManyToManyField(Post)
    

    class Meta:
        verbose_name = "Favourite"
        verbose_name_plural = "Favourites"

    def __str__(self):
        return 'favourites@'+str(self.owner)

    def get_absolute_url(self):
        return reverse("Favourite_detail", kwargs={"pk": self.pk})
