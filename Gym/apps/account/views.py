 
 
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,CreateView
from apps.Blog.models import Article
from .mixin import FieldsMixin,FormValidMixin
# Create your views here.
class ArticleList(LoginRequiredMixin,ListView):
    template_name='registration/home.html'
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)
        
class ArticleCreate(LoginRequiredMixin,FormValidMixin,FieldsMixin,CreateView):
    model= Article
    template_name='registration/Article-create-update.html'
     