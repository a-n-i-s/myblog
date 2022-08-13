from sys import displayhook
from django.contrib import admin
from .models import Catagory, Comment,Post
from django.utils.html import format_html
# Register your models here.

class CommentInline(admin.StackedInline):
    model=Comment
    fields=['owner','created_at','parent','body']
    readonly_fields=['owner','created_at']
    extra=1
    

    



    
    
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
    inlines=[CommentInline]
    @admin.display(description='')
    def get_title(self,obj):
        return 'see more'

    def save_formset(self, request, form, formset, change):
        instances=formset.save(commit=False)
        for c in instances:
            c.owner=request.user
            c.save()
        return super().save_formset(request, form, formset, change)






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


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model=Comment
    list_display=['body','post','parent','owner','created_at','updated_at']
    list_filter=['post','parent','owner','created_at']
    search_fields=['title','body']
    fields=[(('post','parent','owner')),('created_at','updated_at'),'body',]
    readonly_fields=['created_at','updated_at','owner']
    
    def get_readonly_fields(self, request, obj):
        read_only_fields=super().get_readonly_fields(request, obj)
        if obj==None:
            return read_only_fields
        if request.user!=obj.post.author.user:
            read_only_fields.append('body')

        return read_only_fields+['parent','post']

    def save_model(self, request, obj, form, change):
        obj.owner=request.user
        print("okokokoko")
        return super().save_model(request, obj, form, change)
    