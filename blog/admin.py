from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display=('title','author','sort_description','last_updated')
	list_filter=('author','last_updated')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display=('name','post_count')
admin.site.register(Comment)

