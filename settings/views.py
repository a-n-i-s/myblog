from audioop import reverse
from django.shortcuts import render
from django.views.generic import UpdateView
from .models import UserSetting,AuthorSetting
from django.urls import reverse_lazy
# Create your views here.

class SettingsUpdateView(UpdateView):
    model=UserSetting
    fields='__all__'
    template_name = "settings/settings.html"
    
    def get_success_url(self):
        return "/"
    
    def get_queryset(self):
        return super().get_queryset()
    
