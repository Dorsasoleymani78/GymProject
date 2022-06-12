from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator 
# Create your views here.
from .models import Article,Category
from django.views.generic import ListView,DetailView
from apps.account.models import User
# def show_articles(request,page=1):
#     articleList=Article.objects.published() 
#     paginator = Paginator(articleList,2)
    
#     articles = paginator.get_page(page)
#     context={
#         "articles":articles
         
#         }
#     return render(request,'Blog/home.html',context)
class ArticleList(ListView):
    queryset= Article.objects.published() 
    paginate_by=2
    context_object_name="articles"
    template_name='Blog/article_list.html'

# def detail_article(request,slug):
#     context={
#         'article': get_object_or_404(Article.objects.published(),slug=slug,status='Publish')
#     }
#     return render(request,'Blog/detail.html',context)

class ArticleDetail(DetailView):
    def get_object(self ) :
        slug=self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(),slug=slug,status='Publish')

# def category(request,slug,page=1):
#     category= get_object_or_404(Category,slug=slug,status=True)
#     articleList=category.articles.published()
#     paginator = Paginator(articleList,3)
#     articles = paginator.get_page(page)
#     context={
#          'category': category,
#          'articles':articles
#     }
#     return render(request,'Blog/category.html',context)

class CategoryList(ListView):
    paginate_by=2
    template_name='Blog/category_list.html'
    context_object_name="articles"
    def get_queryset(self)  :
        global category
        slug=self.kwargs.get('slug')
        category= get_object_or_404(Category.objects.active(),slug=slug )
        return  category.articles.published()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context
    
class AuthorList(ListView):
    paginate_by=2
    template_name='Blog/User_list.html'
 
    def get_queryset(self)  :
        global author
        username=self.kwargs.get('username')
        author= get_object_or_404(User,username=username)
        return  author.articles.published()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context
    