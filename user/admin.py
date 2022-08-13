from atexit import register
from django.contrib import admin
from .models import Author,User,AuthorRequest
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(User)    
class UserAdmin(admin.ModelAdmin):
    pass

@admin.action()
def aprove(ModelAdmin,request,queryset):
    for d in queryset:
        Author.objects.create(
            user=d.user,
            name=d.name,
            about=d.about,
            status=d.status
        )
        d.delete()

@admin.action()
def block(ModelAdmin,request,queryset):
    queryset.update(status=1)

    


@admin.register(AuthorRequest)
class AuthorRequestAdmin(admin.ModelAdmin):

    actions=[aprove,block]
    ordering=['status']
    
