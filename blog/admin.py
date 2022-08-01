from django.contrib import admin
from .models import Tag,Catagory,Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
            ('title'),
            ('author','catagory'),
            ('created_at','updated_at','hits'),          
            ),
            
        }),
        (None, {
            "fields": (
            'body',          
            ),
        }),
        
        (None, {
            "fields": (
            'tags',          
            ),
        }),
        
    )
    
    
    readonly_fields=['created_at','updated_at','hits']

@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

