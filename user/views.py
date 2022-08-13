from multiprocessing import get_context
from django.shortcuts import render,redirect
from .models import Author,AuthorRequest
from django.views.generic import DetailView,CreateView,UpdateView
from django.urls import reverse_lazy

def get_author(x):
      try:
        return x.author
      except:
        return None

def get_request(x):
      try:
        return x.request
      except:
        return None
# Create your views here.
class AuthorDetailView(DetailView):
    model = Author
    template_name = "author/authordetail.html"

class AuthorRequestView(CreateView):
    model = AuthorRequest
    fields=['name','about']
    template_name = "author/authorrequest.html"

    def form_valid(self,form,**kwargs):
      form.instance.user=self.request.user
      return super().form_valid(form,**kwargs)
    
    def get_success_url(self):
       return reverse_lazy('authorrequest_status',args=[self.object.id])

    
    def get(self, request ,*args, **kwargs):
      
      if get_author(request.user):
        return redirect('post_create')

      r=get_request(request.user)
      
      if r:
        return redirect('authorrequest_status',r.id)
    
      
      return super().get(request, *args, **kwargs)

def authorrequeststatus(request,pk):
  r=None
  try:
    r=AuthorRequest.objects.get(pk=pk)
  except:
    pass
  if not r:
    return redirect('post_list')
  context={
    'request':r
  }
  return render(request,template_name='author/authorrequeststatus.html',context=context)


class AuthorUpdateView(UpdateView):
  model = Author
  fields = ['name','about']
  template_name = "author/authorupdate.html"


  def get_context_data(self, **kwargs):
     return super().get_context_data(**kwargs)