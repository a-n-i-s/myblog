from sys import displayhook
from django.contrib import admin
from .models import Catagory,Post
from django.utils.html import format_html
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Post', {
            "fields": (
            ('title','author','body',),
            ),
            
        }),
        
        ('Catagoty and Tags', {
            "fields": (
            'catagory',
            'tags',          
            ),
        }),

        ('More Info', {
            "fields": (
                      
            
            ('created_at','updated_at','hits'),          
            
            ),
        }),


        
        
    )
    
    readonly_fields=['created_at','updated_at','hits']
    list_display=['title','author','created_at','updated_at','catagory','hits','get_title']
    
    sortable_by=['title','author','created_at','updated_at','catagory','hits',]
    
    list_editable=['title','catagory',]
    list_display_links=['get_title']
    list_filter=['author','updated_at','tags','catagory','hits']
    search_fields=['title','body']

    @admin.display(description='')
    def get_title(self,obj):
        return 'see more'

class PostInline(admin.StackedInline):
    model=Post
    fields = ['get_title','author']
    readonly_fields=fields
    extra=0

    def get_title(self,obj):
        return format_html(f'''<a href=''>{obj.title}</a>''')


@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    fields=['name']
    inlines=[PostInline]

'''@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=['name','get_posts']
    fieldsets = (
        (None, {
            "classes":['wide'],
            "fields": (
                'name',
            ),
        }),
    )
    
    @admin.display(description='id')
    def get_posts(self,obj):
        return obj.id

'''