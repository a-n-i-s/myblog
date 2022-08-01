from django.db import models
from user.models import Author
from django.urls import reverse
# Create your models here.

class Post(models.Model):
  PRIVACY=[
    (0,'public'),
    (1,'readers only'),
  ]
  
  title=models.CharField(max_length=200)
  body=models.TextField()
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)
  author=models.ForeignKey(Author,on_delete=models.CASCADE)
  hits=models.IntegerField(default=0,editable=False)
  privacy=models.IntegerField(choices=PRIVACY,default=0)
  tags=models.ManyToManyField('Tag',blank=True)
  catagory=models.ForeignKey('Catagory',on_delete=models.CASCADE)
  def __str__(self):
      return self.title

  def get_absolute_url(self):
      return reverse("post_detail", kwargs={"pk": self.pk})



class Tag(models.Model):

    name=models.CharField(max_length=100)

    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Tag_detail", kwargs={"pk": self.pk})

class Catagory(models.Model):
    parent=models.ForeignKey('self',null=True,blank=True,default=None,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)

    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Catagory_detail", kwargs={"pk": self.pk})
