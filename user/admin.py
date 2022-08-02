from atexit import register
from django.contrib import admin
from .models import Author,User
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(User)    
class UserAdmin(admin.ModelAdmin):
    pass

