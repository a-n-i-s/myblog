from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.
class Ad(models.Model):

    link=models.URLField()
    body=RichTextField()

    class Meta:
        verbose_name = "Ad"
        verbose_name_plural = "Ads"

    def __str__(self):
        return 'ad #' + str(self.id)

    def get_absolute_url(self):
        return reverse("Ad_detail", kwargs={"pk": self.pk})
