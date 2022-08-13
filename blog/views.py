from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import Catagory, Post,Author,Comment
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = "post/posts.html"
    
    
class PostDetailView(DetailView):
    model = Post
    template_name = "post/postdetail.html"

class PostCreateView(CreateView):
    model = Post
    fields=['title','body','catagory','tags']
    template_name = "post/postcreate.html"

    def form_valid(self,form):
        form.instance.author=self.request.user.author
        return super().form_valid(form)

    



class PostUpdateView(UserPassesTestMixin,UpdateView):
    model = Post
    fields=['title','body','catagory','tags']
    template_name = "post/postcreate.html"
    
    def test_func(self):
        return self.get_object().author.user==self.request.user

    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        data['edit']=True
        return data
class PostDeleteView(DeleteView):
    model = Post
    template_name = "post/postdelete.html"
    success_url=reverse_lazy('post_list')



       



class CommentListView(ListView):
    model = Comment
    template_name = "Comment/Comments.html"
    queryset=Comment.objects.filter(parent=None)
    
    

class CommentCreateView(CreateView):
    model = Comment
    fields=['body']
    template_name = "comment/commentcreate.html"
    
    def get_success_url(self):
        
        return reverse_lazy('post_detail',args={self.object.post.id})
    def form_valid(self,form):
        form.instance.owner=self.request.user
        form.instance.post=Post.objects.get(pk=self.kwargs.get('pk'))
        parent_id=self.request.POST.get('parent',None)
        if parent_id:
            form.instance.parent=get_object_or_404(Comment,id=parent_id)
        print(self.request.POST)
        return super().form_valid(form)

    



class CommentUpdateView(UserPassesTestMixin,UpdateView):
    model = Comment
    fields=['body']
    template_name = "comment/commentcreate.html"
    
    def test_func(self):
        return self.get_object().owner==self.request.user

    def get_success_url(self):
        
        return reverse_lazy('post_detail',args={self.object.post.id})
    
    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        data['edit']=True
        return data

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = "comment/commentdelete.html"
    
    def get_success_url(self):
        
        return reverse_lazy('post_detail',args={self.object.post.id})
   

class CatagoryDetailView(DetailView):
    model=Catagory
    template_name='post/catagory_detail.html'
       










